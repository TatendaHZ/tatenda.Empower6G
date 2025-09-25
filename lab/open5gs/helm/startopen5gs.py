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

# Step 4: Patch all *-cmap.yaml files
for filename in os.listdir(template_dir):
    if not filename.endswith("cmap.yaml"):
        continue

    full_path = os.path.join(template_dir, filename)
    with open(full_path, "r") as f:
        content = f.read()

    original_content = content

    for svc_name, ip in svc_ip_map.items():
        # Special case: NRF line 'name: nrf-svc' → 'addr: <ip>'
        if svc_name == "nrf-svc":
            content = re.sub(r"(name:\s*)nrf-svc", fr"addr: {ip}", content)

        # General case: replace exact service name appearances
        content = re.sub(
            rf"(?<![\w\-]){re.escape(svc_name)}(?![\w\-])", 
            ip, 
            content
        )

    # Only write if changes occurred
    if content != original_content:
        with open(full_path, "w") as f:
            f.write(content)
        print(f"✏️  Updated: {filename}")
    else:
        print(f"✅ No changes in: {filename}")

print("🏁 Done: All cmap YAML files updated with actual IPs.")
