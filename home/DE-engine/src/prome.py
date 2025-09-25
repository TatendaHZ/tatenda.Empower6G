import asyncio
import json
import requests
import time

# Configuration
INTERVAL = 30  # Data sending interval in seconds
PROMETHEUS_NODE_IP = "192.168.2.6"  # Replace with kube-master or any node IP
PROMETHEUS_PORT = "30041"

PROMETHEUS_URL = f"http://{PROMETHEUS_NODE_IP}:{PROMETHEUS_PORT}/api/v1/query"

NODES = [
    {"name": "core node", "ip": "192.168.2.9:9100"},
    {"name": "mec node", "ip": "192.168.2.10:9100"},
    {"name": "kube-app-server", "ip": "192.168.2.6:9100"}
]

async def fetch_metrics(node):
    try:
        cpu_expr = f"avg(100 - ((rate(node_cpu_seconds_total{{job=\"node-exporter\",instance=\"{node['ip']}\",mode=\"idle\"}}[1m])) * 100))"
        mem_expr = f"100 - (avg(node_memory_MemAvailable_bytes{{job=\"node-exporter\", instance=\"{node['ip']}\"}}) / avg(node_memory_MemTotal_bytes{{job=\"node-exporter\", instance=\"{node['ip']}\"}}) * 100)"
        tx_expr = f"rate(node_network_transmit_bytes_total{{job=\"node-exporter\", instance=\"{node['ip']}\", device=\"enp0s3\"}}[1m]) * 8"
        rx_expr = f"rate(node_network_receive_bytes_total{{job=\"node-exporter\", instance=\"{node['ip']}\", device=\"enp0s3\"}}[1m]) * 8"

        response = {
            "cpu": requests.get(PROMETHEUS_URL, params={"query": cpu_expr}).json()["data"]["result"][0]["value"][1],
            "memory": requests.get(PROMETHEUS_URL, params={"query": mem_expr}).json()["data"]["result"][0]["value"][1],
            "tx": requests.get(PROMETHEUS_URL, params={"query": tx_expr}).json()["data"]["result"][0]["value"][1],
            "rx": requests.get(PROMETHEUS_URL, params={"query": rx_expr}).json()["data"]["result"][0]["value"][1],
            "latency": "1.0",  # Placeholder
            "cost": "4"        # Placeholder
        }
        return {node["name"]: response}
    except Exception as e:
        print(f"Error fetching metrics for {node['name']}: {e}")
        return {node["name"]: {"cpu": 0, "memory": 0, "tx": 0, "rx": 0, "latency": 0, "cost": 0}}

async def print_data(data):
    payload = {
        "execution_plugin": "ComputeNode",
        "parameters": {
            "telemetry": [value for node in data for value in [node]]
        }
    }
    print(json.dumps(payload, indent=4))

async def main():
    while True:
        data = await asyncio.gather(*(fetch_metrics(node) for node in NODES))
        await print_data(data)
        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
