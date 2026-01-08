import paramiko
import time
from io import StringIO

# ----------------------------------------------
# CONFIGURATION
# ----------------------------------------------
VM_HOST = "192.168.10.11"
VM_USER = "generic"
VM_PASSWORD = "11387333"
VM_FILE = "/home/generic/tatenda.Empower6G/office/DE-engine/src/seven_days_metrics.csv"

SERVER_HOST = "195.251.58.122"
SERVER_PORT = 2315
SERVER_USER = "user"
SERVER_PATH = "/home/user/work/autoencoder/tatenda.Empower6G/office/DE-engine/src/daily_metrics/second_batch/seven_days_metrics.csv"

# SET MODE: "full" to copy full file | "append" to append only last line
COPY_MODE = "full"   # change to "append" if needed

INTERVAL = 10   # seconds


# ----------------------------------------------
# SSH HELPERS
# ----------------------------------------------

def ssh_connect(host, user, password=None, port=22):
    """Create an SSH client connection"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if password:
        client.connect(host, port=port, username=user, password=password)
    else:
        client.connect(host, port=port, username=user)
    return client


def sftp_download(client, remote_path):
    """Download file content from remote machine"""
    sftp = client.open_sftp()
    with sftp.file(remote_path, 'r') as f:
        return f.read().decode()
    

def sftp_upload_content(client, content, remote_path):
    """Upload text content to remote file"""
    sftp = client.open_sftp()
    with sftp.file(remote_path, 'w') as f:
        f.write(content)
    sftp.close()


def sftp_append_content(client, content, remote_path):
    """Append text to file on server"""
    sftp = client.open_sftp()
    with sftp.file(remote_path, 'a') as f:
        f.write(content)
    sftp.close()


# ----------------------------------------------
# MAIN LOOP
# ----------------------------------------------

print("Starting metrics sync every 10 seconds...")

while True:
    try:
        # ---- CONNECT TO VM AND GET CSV ----
        vm_client = ssh_connect(VM_HOST, VM_USER, VM_PASSWORD)
        csv_data = sftp_download(vm_client, VM_FILE)
        vm_client.close()

        # ---- PROCESS FOR APPEND MODE ----
        if COPY_MODE == "append":
            last_line = csv_data.strip().split("\n")[-1] + "\n"
            content_to_upload = last_line
        else:
            content_to_upload = csv_data

        # ---- CONNECT TO SERVER AND UPLOAD ----
        server_client = ssh_connect(SERVER_HOST, SERVER_USER, port=SERVER_PORT)
        
        if COPY_MODE == "append":
            sftp_append_content(server_client, content_to_upload, SERVER_PATH)
            print("✔ Appended last line to server.")
        else:
            sftp_upload_content(server_client, content_to_upload, SERVER_PATH)
            print("✔ Uploaded full file to server.")

        server_client.close()

    except Exception as e:
        print("❌ ERROR:", e)

    # ---- WAIT BEFORE NEXT UPDATE ----
    time.sleep(INTERVAL)
