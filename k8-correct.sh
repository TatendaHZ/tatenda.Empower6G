#!/bin/bash

FILE="/etc/kubernetes/manifests/kube-apiserver.yaml"
FLAG="--service-node-port-range=1024-65535"

# Check if already present
if grep -q "$FLAG" "$FILE"; then
    echo "Flag already present."
    exit 0
fi

# Insert after the --secure-port line
sudo sed -i "/- --secure-port=6443/a\    - $FLAG" "$FILE"

echo "Flag added. kubelet will restart kube-apiserver automatically."
