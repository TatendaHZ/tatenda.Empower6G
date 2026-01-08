
## 📋 Prerequisites

Before starting, ensure you have the following:

* Ubuntu-based system (VM or bare metal)
* Python 3
* Docker
* Helm
* Kubernetes tools (`kubeadm`, `kubectl`, `kubelet`)
* Stable internet access

---

## 🚀 Step 1: Kubernetes & Calico Setup

The first step is setting up **Kubernetes** and the **Calico CNI**.

📺 **Follow this video carefully to prepare your system:**
👉 [https://www.youtube.com/watch?v=EHDDm_iR1Fs](https://www.youtube.com/watch?v=EHDDm_iR1Fs)

This includes:

* Kubernetes cluster initialization
* Network configuration
* Calico installation

---

## 🔄 Restarting the System (Optional)

Once Kubernetes is correctly set up, you can restart the entire platform at any time using:

```bash
sudo swapoff -a
```

```bash
python3 setupk8.py
```

This script **reinitializes the Kubernetes environment**.

---

## 🔓 Step 2: Enable Required Network Ports

To allow Kubernetes to use **5G-related ports** (e.g. **2152 / GTP-U**), run:

```bash
sudo ./k8-correct.sh
```

⚠️ **This step is mandatory** for proper **Open5GS UPF functionality**.

---

## 🌐 Step 3: Update Network IPs

Update the **UPF IP addresses** based on the active network:

```bash
python3 update_ips.py
```

This ensures UPFs are correctly configured regardless of the network environment.

---

## 📊 Step 4: Monitoring Stack (Prometheus & Grafana)

### Navigate to the monitoring directory

```bash
cd /home/generic/tatenda.Empower6G/office/monitoring
```

### Create the monitoring namespace

```bash
kubectl create -f namespace.yaml
```

### Expose Grafana and Prometheus

```bash
kubectl apply -f grafana-nodeport-svc.yaml
kubectl apply -f prometheus-nodeport-svc.yaml
```

### Install Prometheus Stack via Helm

```bash
helm install prometheus prometheus-community/kube-prometheus-stack \
  --version 45.7.1 \
  --namespace monitoring
```

---

## 🧠 Step 5: Open5GS Core Deployment

### Create Open5GS namespace

```bash
cd /home/generic/tatenda.Empower6G/office/open5gs
kubectl create -f namespace.yaml
```

### Set Open5GS as default namespace

```bash
kubectl config set-context --current --namespace=open5gs
```

### Deploy Open5GS Core Network

```bash
cd /home/generic/tatenda.Empower6G/office/open5gs/helm
helm -n open5gs install -f values.yaml 5gcore ./
```

This launches the **full Open5GS 5G Core** inside Kubernetes.

---

## 📡 Step 6: UERANSIM Integration

The platform supports **UERANSIM** for UE and gNB emulation.

📘 **Installation Guide:**
👉 [https://medium.com/rahasak/5g-core-network-setup-with-open5gs-and-ueransim-cd0e77025fd7](https://medium.com/rahasak/5g-core-network-setup-with-open5gs-and-ueransim-cd0e77025fd7)

Follow the guide carefully to install and build UERANSIM.

### Required Files & Directories on the UERANSIM VM

Ensure the following paths and files exist:

1. **Scraping Script**
   `/home/ueransim/scrap.py`

2. **API Test Server**
   `/home/ueransim/test_api/server.py`

---

### Connecting UERANSIM to Open5GS

Navigate to the UERANSIM directory:

```bash
cd /home/ueransim/UERANSIM
```

Start the **gNB**:

```bash
./build/nr-gnb -c config/open5gs-gnb.yaml
```

Start the **UE**:

```bash
sudo ./build/nr-ue -c config/open5gs-ue.yaml
```

---

### Start Auxiliary Services

In separate terminals, run:

```bash
sudo python3 /home/ueransim/test_api/server.py
sudo python3 /home/ueransim/scrap.py
```

---

## 📈 Step 7: Data Collection & ML Metrics Engine

To collect and process system metrics:

```bash
cd /home/generic/tatenda.Empower6G/office/DE-engine/src
sudo python3 mlmetric5day.py
```

This component handles:

* Metrics aggregation
* Data preprocessing
* ML-ready output for further analysis

---

## 🤖 Step 8: Machine Learning & Anomaly Detection Pipeline

### Transfer Metrics to the Server

First, transfer collected metrics to the ML server: This is done on the windows machine 
```bash
cd \Users\User\Desktop\server
```

```bash
python3 transfer_metrics.py
```

---

### Train the Models

On the server, locate and run: on the windows machine
```bash
ssh user@195.251.58.122 -p 2315
```
```bash
cd /home/user/work/autoencoder/tatenda.Empower6G/office/DE-engine/src/daily_metrics
source second_batch_venv/bin/activate
```
```bash
cd /home/user/work/autoencoder/tatenda.Empower6G/office/DE-engine/src/daily_metrics/second_batch
```
This step is optional since training has been done already
```bash
#python3 train_region_autoencoder.py
```

This trains region-based autoencoder models and stores them for inference.

---

### Enable Live Anomaly Detection

Run the real-time detector:

```bash
sudo python3 realtime_detector.py
```

This enables live anomaly detection and streaming inference.

---

## 🎥 Step 9: CAMARA & NEF Integration

### CAMARA QoD Playground

CAMARA is based on:
[https://github.com/Fundacio-i2CAT/ASSessionWithQoS/blob/master/docs/deployment.md](https://github.com/Fundacio-i2CAT/ASSessionWithQoS/blob/master/docs/deployment.md)

⚠️ Custom modifications were applied to support multiple users.

---

### NEF + CAMARA QoD Deployment

```bash
cd /home/generic/tatenda.Empower6G/NEFwQoS
kubectl apply -f nef-qod-deployment.yaml
```

---

### PCC Rule Configuration

Before launching NEF, update **PCC rules** via the Open5GS WebUI as described in the CAMARA documentation.

---

### CAMARA Session Management

```bash
cd /home/generic/tatenda.Empower6G/office/DE-engine/src/camara
```

Scripts available:

* `create_session.py`
* `delete_session.py`
* `session.py`
* `session_info.txt`

---

## 🎚️ Network Gain Control

```bash
cd /home/generic/tatenda.Empower6G/office/DE-engine/src/gain
```

Run one of the following:

```bash
python3 change_gain.py low
python3 change_gain.py medium
python3 change_gain.py high
python3 change_gain.py max
```

---

## ✅ Final Checks

```bash
kubectl get pods -A
```

Verify:

* All pods are running
* Grafana and Prometheus NodePorts are reachable
* UERANSIM successfully registers with Open5GS

---

## 🧪 Troubleshooting

* Restart Kubernetes using `setupk8.py`
* Re-run `k8-correct.sh` if GTP traffic fails
* Check UPF logs if UE has no data connectivity

---

## 📌 License & Credits

This setup integrates:

* Open5GS
* UERANSIM
* Kubernetes
* Prometheus & Grafana

All third-party tools follow their respective licenses.
