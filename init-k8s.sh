#!/bin/bash

set -e

echo "🔧 Installing containerd (if needed)..."
sudo apt-get update
sudo apt-get install -y containerd

sudo systemctl enable containerd
sudo systemctl start containerd

echo "🧹 Cleaning up stale Kubernetes processes (if any)..."
sudo systemctl stop kubelet || true
sudo pkill -f kube-apiserver || true
sudo pkill -f etcd || true

echo "🚀 Initializing Kubernetes cluster..."
sudo kubeadm init --control-plane-endpoint 192.168.10.11:6443 --pod-network-cidr 10.10.0.0/16

echo "🛠 Setting up kubeconfig for current user..."
mkdir -p $HOME/.kube
sudo cp -f /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

echo "⏳ Waiting for kube-apiserver to be ready..."
until kubectl get --raw='/readyz' &>/dev/null; do
    sleep 2
done
echo "✅ kube-apiserver is ready."

echo "📦 Applying Calico network plugin..."
kubectl apply -f calico.yaml
