import subprocess
import sys
import paramiko
import time

# Worker node credentials
WORKER_NODES = [
    {"host": "192.168.2.7", "user": "generc", "pass": "11387333"},
    {"host": "192.168.2.6", "user": "generic", "pass": "11387333"},
    {"host": "192.168.2.8", "user": "generic", "pass": "11387333"}
]

def print_step(msg):
    print(f"\n🟡 {msg}")

def print_done(msg):
    print(f"✅ {msg}\n")

def run_script_quiet(script_path):
    print_step(f"Running {script_path}...")
    try:
        result = subprocess.run([script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        print_done(f"Finished {script_path}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script_path}. Exit code: {e.returncode}")
        sys.exit(1)

def extract_join_command(output):
    lines = output.splitlines()
    join_cmd = []
    capture = False
    for line in lines:
        if line.startswith("kubeadm join"):
            capture = True
        if capture:
            join_cmd.append(line.strip().rstrip("\\").strip())
            if not line.endswith("\\"):
                break
    return " ".join(join_cmd)

def wait_for_master_ready(timeout=180):
    print_step("Waiting for master node to become Ready...")
    for _ in range(timeout // 5):
        try:
            result = subprocess.run(["kubectl", "get", "nodes", "--no-headers"], capture_output=True, text=True)
            output = result.stdout.strip()
            if "Ready" in output:
                print_done("Master node is Ready")
                return
        except Exception:
            pass
        time.sleep(5)
    print("❌ Timeout waiting for master node to become Ready.")
    sys.exit(1)

def ssh_and_run_commands(host, user, password, commands):
    print_step(f"Connecting to {host} as {user} via SSH...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username=user, password=password)
    except Exception as e:
        print(f"❌ SSH connection failed: {e}")
        sys.exit(1)

    for cmd in commands:
        print_step(f"Running on {host}: {cmd}")
        full_cmd = f"echo '{password}' | sudo -S {cmd}"
        stdin, stdout, stderr = ssh.exec_command(full_cmd)
        exit_status = stdout.channel.recv_exit_status()
        out = stdout.read().decode()
        err = stderr.read().decode()
        if exit_status != 0:
            print(f"⚠️ Command failed: {cmd}")
            print(err)
        else:
            print(out)

    ssh.close()
    print_done(f"Finished running commands on {host}")

if __name__ == "__main__":
    run_script_quiet("./remove-k8s.sh")
    run_script_quiet("./install-k8s.sh")
    run_script_quiet("./k8-correct.sh")
    init_output = run_script_quiet("./init-k8s.sh")

    join_command = extract_join_command(init_output)
    if join_command:
        print(f"\n📌 Join command extracted:\n{join_command}\n")
        with open("join-command.sh", "w") as f:
            f.write("#!/bin/bash\n")
            f.write(join_command + "\n")
    else:
        sys.exit("❌ kubeadm join command not found.")

    wait_for_master_ready()

    for node in WORKER_NODES:
        ssh_and_run_commands(node["host"], node["user"], node["pass"], [
            "kubeadm reset -f",
            join_command
        ])

    print("🎉 All worker nodes joined successfully.")
