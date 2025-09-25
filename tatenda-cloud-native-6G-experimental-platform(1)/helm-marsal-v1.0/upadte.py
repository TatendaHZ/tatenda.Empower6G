import subprocess
import os
import re
import time

# --- Config ---
namespace = "open5gs"
release_name = "5gcore"
helm_values = "values.yaml"
helm_chart_dir = "./"
template_dir = "./templates/core"
webui_depl_file = "webui-depl.yaml"

# Step 1: Run Helm install
print("⎈ Installing Helm chart...")
try:
    subprocess.run(
        ["helm", "-n", namespace, "install", "-f", helm_values, release_name, helm_chart_dir],
        check=True
    )
except subprocess.CalledProcessError:
    print("❌ Helm install failed.")
    exit(1)

# Step 2: Wait for services to appear
print("⏳ Waiting for services to be available...")
while True:
    try:
        svc_output = subprocess.check_output(["kubectl", "-n", namespace, "get", "svc"], text=True)
        if "amf-svc" in svc_output:
            break
        time.sleep(2)
    except subprocess.CalledProcessError:
        time.sleep(2)

print("✅ Services are up. Processing YAML updates...")

# Step 3: Build service name -> IP mapping
svc_ip_map = {}
for line in svc_output.strip().split("\n")[1:]:
    columns = re.split(r"\s+", line)
    if len(columns) >= 3:
        name = columns[0]
        ip = columns[2]
        svc_ip_map[name] = ip

# Step 4: Update all *-cmap.yaml files
for filename in os.listdir(template_dir):
    if not filename.endswith("cmap.yaml"):
        continue

    full_path = os.path.join(template_dir, filename)
    with open(full_path, "r") as f:
        content = f.read()

    original_content = content

    for svc_name, ip in svc_ip_map.items():
        # --- Custom rules ---
        if svc_name == "nrf-svc":
            content = re.sub(
                r"(?m)^\s*- name:\s*nrf-svc\b",
                f"- addr: {ip}",
                content
            )

        if svc_name == "bsf-svc":
            content = re.sub(
                r"(?m)^\s*- name:\s*bsf-svc\b",
                f"- addr: {ip}",
                content
            )

        if svc_name == "af-svc":
            content = re.sub(
                rf"\b{re.escape(svc_name)}\b",
                ip,
                content
            )

        # --- Original rule ---
        content = re.sub(
            rf"\b{re.escape(svc_name)}\b",
            ip,
            content
        )

    if content != original_content:
        with open(full_path, "w") as f:
            f.write(content)
        print(f"✏️  Updated: {filename}")
    else:
        print(f"✅ No changes in: {filename}")

# Step 5: Update webui-depl.yaml only
webui_path = os.path.join(template_dir, webui_depl_file)
if os.path.exists(webui_path):
    with open(webui_path, "r") as f:
        content = f.read()

    original_content = content

    for svc_name, ip in svc_ip_map.items():
        content = re.sub(
            rf"\b{re.escape(svc_name)}\b",
            ip,
            content
        )

    if content != original_content:
        with open(webui_path, "w") as f:
            f.write(content)
        print(f"✏️  Updated: {webui_depl_file}")
    else:
        print(f"✅ No changes in: {webui_depl_file}")
else:
    print(f"⚠️  webui-depl.yaml not found in {template_dir}")

print("🏁 Done: All YAML files updated with actual service IPs.")
