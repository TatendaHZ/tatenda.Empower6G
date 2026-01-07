import subprocess
import re
import json

# ------------------------------
# 1. Get live node IPs from kubectl
# ------------------------------
def get_node_ips():
    result = subprocess.run(['kubectl', 'get', 'nodes', '-o', 'wide'],
                            capture_output=True, text=True)
    node_ips = {}
    lines = result.stdout.strip().split('\n')[1:]  # skip header
    for line in lines:
        parts = line.split()
        node_ips[parts[0]] = parts[5]  # internal IP
    return node_ips

node_ips = get_node_ips()
kube_app_server_ip = node_ips.get('kube-worker1')  # AS node
kube_core_ip = node_ips.get('kube-core')           # Core UPF
kube_mec_ip = node_ips.get('kube-mec')             # MEC UPF

# ------------------------------
# 2. Helper function to replace any IP after a pattern safely
# ------------------------------
def replace_ip_in_file(file_path, pattern, new_ip):
    with open(file_path, 'r') as f:
        content = f.read()

    escaped_pattern = re.escape(pattern)

    # Replace any IP after the pattern using a lambda
    content_new = re.sub(
        rf'({escaped_pattern}\s*:\s*)\d{{1,3}}(?:\.\d{{1,3}}){{3}}',
        lambda m: m.group(1) + new_ip,
        content
    )

    with open(file_path, 'w') as f:
        f.write(content_new)

# ------------------------------
# 3. Special function for as-depl.yaml /shared/ line
# ------------------------------
def replace_shared_ip(file_path, new_ip):
    with open(file_path, 'r') as f:
        content = f.read()

    # Replace any IP after "/shared/" in mkdir -p commands
    content_new = re.sub(
        r'(/shared/localhost\s*/shared/)\d{1,3}(?:\.\d{1,3}){3}',
        lambda m: m.group(1) + new_ip,
        content
    )

    with open(file_path, 'w') as f:
        f.write(content_new)

# ------------------------------
# 4. Update AS Deployment (as-depl.yaml)
# ------------------------------
#as_depl_file = '/home/generic/tatenda.Empower6G/office/open5gs/helm/templates/core/as-depl.yaml'
#replace_shared_ip(as_depl_file, kube_app_server_ip)

# ------------------------------
# 5. Update Core UPF (upf-cmap.yaml)
# ------------------------------
upf_cmap_file = '/home/generic/tatenda.Empower6G/office/open5gs/helm/templates/core/upf-cmap.yaml'
replace_ip_in_file(upf_cmap_file, 'advertise', kube_core_ip)

# ------------------------------
# 6. Update MEC UPF (upfmec-cmap.yaml)
# ------------------------------
upfmec_cmap_file = '/home/generic/tatenda.Empower6G/office/open5gs/helm/templates/mec/upfmec-cmap.yaml'
replace_ip_in_file(upfmec_cmap_file, 'advertise', kube_mec_ip)

# ------------------------------
# 7. Update streams.json
# ------------------------------
streams_file = '/home/generic/tatenda.Empower6G/office/open5gs/helm/files/streams.json'
with open(streams_file, 'r') as f:
    streams_data = json.load(f)

streams_data['streams']['vod']['distributionConfigurations'][0]['domainNameAlias'] = kube_app_server_ip

with open(streams_file, 'w') as f:
    json.dump(streams_data, f, indent=2)  # preserve formatting

# ------------------------------
# 8. Done
# ------------------------------
print("✅ All IP addresses updated successfully:")
print(f"   AS node IP       -> {kube_app_server_ip}")
print(f"   Core UPF IP      -> {kube_core_ip}")
print(f"   MEC UPF IP       -> {kube_mec_ip}")
