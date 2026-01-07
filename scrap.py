import subprocess
import time
import statistics
import requests
from scapy.all import IP, ICMP, sr1, conf

# Configuration
interfaces = ["uesimtun0", "uesimtun1"]
target_ip = "192.168.88.40"
api_url = "http://192.168.88.46/post_metrics"
ping_count = 10
timeout = 1  # seconds
interval = 5  # seconds between measurements

def get_active_interfaces():
    active = []
    for iface in interfaces:
        try:
            subprocess.check_output(["ip", "addr", "show", iface])
            active.append(iface)
        except subprocess.CalledProcessError:
            continue
    return active

def ping_interface(iface, target, count=10):
    conf.iface = iface
    latencies = []
    for _ in range(count):
        packet = IP(dst=target)/ICMP()
        start_time = time.time()
        reply = sr1(packet, timeout=timeout, verbose=0)
        if reply:
            rtt = (time.time() - start_time) * 1000  # in ms
            latencies.append(rtt)
        else:
            latencies.append(None)
        time.sleep(0.2)

    latencies = [l for l in latencies if l is not None]
    if not latencies:
        return None, None

    avg_latency = sum(latencies) / len(latencies)
    jitter = statistics.stdev(latencies) if len(latencies) > 1 else 0
    return avg_latency, jitter

def post_results(iface, latency, jitter):
    payload = {
        "interface": iface,
        "latency_ms": latency,
        "jitter_ms": jitter
    }
    try:
        response = requests.post(api_url, json=payload)
        print(f"Posted results for {iface}: {response.status_code}")
    except Exception as e:
        print(f"Failed to post results: {e}")

def main_loop():
    while True:
        active_ifaces = get_active_interfaces()
        if not active_ifaces:
            print("No active interfaces found.")
        for iface in active_ifaces:
            print(f"Pinging via {iface}...")
            latency, jitter = ping_interface(iface, target_ip, ping_count)
            if latency is not None:
                print(f"{iface} - Avg Latency: {latency:.2f} ms, Jitter: {jitter:.2f} ms")
                post_results(iface, latency, jitter)
            else:
                print(f"{iface} - No response from target")
        time.sleep(interval)

if __name__ == "__main__":
    main_loop()
