# C:\run_and_save_metrics.py   ← Run this on Windows (double-click or cmd)
import paramiko
import csv
import json
import time
from datetime import datetime
import io

# === CONFIG ===
VM_HOST = "192.168.10.11"
VM_USER = "generic"
VM_PASSWORD = "11387333"

REMOTE_HOST = "195.251.58.122"
REMOTE_PORT = 2315
REMOTE_USER = "user"
# (Windows already knows how to connect — uses your key or password)

BASE_PATH = "/home/user/work/autoencoder/tatenda.Empower6G/office/DE-engine/src/daily_metrics/second_batch"
GENERAL_PATH = f"{BASE_PATH}/general"
SEVEN_DAYS_FILE = f"{BASE_PATH}/seven_days_metrics.csv"

# Connect to final server (uses your existing Windows SSH config)
print("Connecting to final server (195.251.58.122)...")
remote_ssh = paramiko.SSHClient()
remote_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_ssh.connect(hostname=REMOTE_HOST, port=REMOTE_PORT, username=REMOTE_USER)
remote_sftp = remote_ssh.open_sftp()

# Create folders
for p in [BASE_PATH, GENERAL_PATH]:
    try: remote_sftp.stat(p)
    except:
        cur = ""
        for part in p.split("/")[1:]:
            cur += "/" + part
            try: remote_sftp.stat(cur)
            except: remote_sftp.mkdir(cur)

# Connect to VM
print("Connecting to VM (192.168.10.11)...")
vm_ssh = paramiko.SSHClient()
vm_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm_ssh.connect(hostname=VM_HOST, username=VM_USER, password=VM_PASSWORD)

# Start the original script on the VM
print("Starting metrics collection on VM... (this will run for 7 days)")
print("Live output below:\n" + "="*60)

stdin, stdout, stderr = vm_ssh.exec_command(
    "cd ~/tatenda.Empower6G/office/DE-engine/src && python3 server_mlmetric5day.py"
)

# Read output line by line
buffer = ""
for line in stdout:
    line = line.rstrip()
    print(line)  # ← All original printing appears exactly as before

    buffer += line + "\n"
    if "{" in line and "}" in line:  # rough JSON detection
        try:
            # Extract JSON block
            start = buffer.rfind("{")
            end = buffer.rfind("}") + 1
            json_str = buffer[start:end]
            data = json.loads(json_str)

            # Build CSV row
            row = {"timestamp": datetime.now().timestamp()}
            # nodes
            for node_name, metrics in data.get("nodes", {}).items():
                for k, v in metrics.items():
                    row[f"{node_name}_{k}"] = float(v) if v != "N/A" else 0.0
            # UEs
            for ue in data.get("ues", []):
                ue_id = ue.get("ue_id", 1)
                for k, v in ue.items():
                    if k != "ue_id":
                        row[f"ue{ue_id}_{k}"] = float(v) if isinstance(v, (int, float)) else 0.0

            # Save to both files on final server
            def save_csv(path, row_dict):
                content = b""
                try:
                    with remote_sftp.open(path, "rb") as f:
                        content = f.read()
                except: pass
                buf = io.BytesIO(content or b"")
                writer = csv.DictWriter(io.TextIOWrapper(buf, encoding="utf-8"), fieldnames=row_dict.keys())
                if not content:
                    writer.writeheader()
                writer.writerow(row_dict)
                buf.seek(0)
                with remote_sftp.open(path, "wb") as f:
                    f.write(buf.read())

            save_csv(SEVEN_DAYS_FILE, row)
            today_file = f"{GENERAL_PATH}/daily_metrics_{datetime.now():%Y-%m-%d}.csv"
            save_csv(today_file, row)

            print(f"SAVED → {SEVEN_DAYS_FILE.split('/')[-1]} | daily_metrics_{datetime.now():%Y-%m-%d}.csv")
            buffer = ""  # clear after successful parse
        except:
            pass  # not valid JSON yet, wait for full block

# Cleanup
vm_ssh.close()
remote_ssh.close()
print("Finished.")
