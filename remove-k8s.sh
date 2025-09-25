#!/bin/bash

# Unhold the packages (in case they were marked to prevent updates)
sudo apt-mark unhold kubelet kubeadm kubectl

# Stop kubelet and container runtime
echo "🛑 Stopping kubelet and container runtime..."
sudo systemctl stop kubelet
sudo systemctl stop containerd 2>/dev/null || sudo systemctl stop docker 2>/dev/null

# Kill any running Kubernetes control plane components
echo "🔪 Killing remaining Kubernetes processes..."
sudo pkill -f kube-apiserver
sudo pkill -f kube-controller-manager
sudo pkill -f kube-scheduler
sudo pkill -f etcd

# Unmount projected volumes to avoid 'device busy' errors
echo "🔌 Unmounting mounted Kubernetes volumes..."
sudo find /var/lib/kubelet -type d -name 'kube-api-access-*' -exec umount {} \; 2>/dev/null

# Purge the Kubernetes packages
echo "🧹 Removing Kubernetes packages..."
sudo apt-get purge -y kubelet kubeadm kubectl kubernetes-cni

# Remove unused packages and dependencies
sudo apt-get autoremove -y

# Clean up Kubernetes data directories
echo "🧼 Cleaning up remaining files..."
sudo rm -rf /var/lib/kubelet
sudo rm -rf /var/lib/etcd
sudo rm -rf /etc/kubernetes
sudo rm -rf /etc/kubernetes/manifests
sudo rm -rf /opt/cni
sudo rm -rf /etc/cni
sudo rm -rf ~/.kube

echo "✅ Kubernetes uninstalled and cleaned up successfully."
