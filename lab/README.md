# About the project: OPEN5GS-CORE In Kuberenetes
Experimental framework with over-the-air transmissions that tackles two critical aspects for enhancing the lifecycle management of 5G and beyond networks: cloud-native deployments of 5G core network functions (NFs) and end-to-end monitoring. First, we deploy + Amarisoft Callbox and Prometheus-based monitoring as containerized network functions (CNFs) in a Kubernetes cluster. We then demonstrate the end-to-end monitoring system by showcasing via Grafana dashboards both infrastructure resources and radio metrics.

# What does this folder contain?
This folder contains the steps and code for deloying Open5GS + Amarisoft RAN + end-to-end monitoring via Kubernetes.
We refer the reader to our paper for more details:

Barrachina-Muñoz, S., Payaró, M., Mangues-Bafalluy, J. (2022). Cloud-native 5G experimental platform with over-the-air transmissions and end-to-end monitoring.

## Requirements
- Kubernetes v1.23.0
- containerd 1.5.5
- Calico CNI
- Open5gs Docker image: sbarrachina/open5gs:v2.4.0
- Helm v3

## Steps for Open5GS deployment in Kubernetes:
1. Create computing resources if needed (e.g., through LXC)
2. Deploy Kubernetes cluster with Containerd or Docker
3. Execute following commands
```bash
cd open5gs
kubectl create -f namespace.yaml
kubectl config set-context --current --namespace=open5gs
helm -n open5gs install -f values.yaml 5gcore ./
kubectl -n open5gs get pods
kubectl -n open5gs logs <amf-podname> # grab amf-podname from previous command and put here
```
4. Adding/Deleting subscribers through Mongo DB. Open5GS uses Mongo to share the subscribers list with 5G core components like UDM. **NOTICE**: UEs will not work without the corresponding previously registered user. You may use the WebUI.


# Amarisoft RAN integration
1. Check Amarisoft setup
2. Modify configuration (<code>.cfg</code> files)
- MME/AMF: leave default <code>mme.cfg</code>
- gNB: \amarisoft-marsal-csndsp\amari-core\gnb-amari-core.cfg
- UE (if using Simbox): \amarisoft-marsal-csndsp\amari-core\ue-amari-core.cfg
3. Run service in Callbox:
```bash
# In Callbox
cd /root/enb/config
ln -sfn <path_to_this_gnb.cfg> enb.cfg
service lte restart

# Open5GS AMF logs
12/15 11:41:56.226: [amf] INFO: gNB-S1 accepted[10.1.14.249]:48340 in ng-path module (../src/amf/ngap-sctp.c:107)
12/15 11:41:56.226: [amf] INFO: gNB-N1 accepted[10.1.14.249] in master_sm module (../src/amf/amf-sm.c:592)
12/15 11:41:56.226: [amf] INFO: [Added] Number of gNBs is now 1 (../src/amf/context.c:865)

# Callbox logs
screen -x lte
#type ctrl+a 1 to access enb
(enb) ng
#should see NG connection state: - server=192.168.162.82:38412 state=setup_done PLMN=00101
```

4. Run service in Simbox (if Simbox enabled):
```bash
# In Simbox
cd /root/ue/config
ln -sfn <path_to_this_ue.cfg> ue.cfg
service lte restart

# Power UE on
screen -x lte
(ue) ue
(ue) power_on 1

# Open5GS AMF logs
12/15 11:42:48.034: [amf] INFO: InitialUEMessage (../src/amf/ngap-handler.c:349)
12/15 11:42:48.034: [amf] INFO: [Added] Number of gNB-UEs is now 1 (../src/amf/context.c:1829)
12/15 11:42:48.034: [amf] INFO:     RAN_UE_NGAP_ID[1] AMF_UE_NGAP_ID[18] TAC[1] CellID[0x1234501] (../src/amf/ngap-handler.c:480)
12/15 11:42:48.034: [amf] INFO: [suci-0-001-01-0-0-0-0000000000] known UE by SUCI (../src/amf/context.c:1300)
12/15 11:42:48.034: [gmm] INFO: Registration request (../src/amf/gmm-sm.c:131)
12/15 11:42:48.034: [gmm] INFO: [suci-0-001-01-0-0-0-0000000000]    SUCI (../src/amf/gmm-handler.c:72)
12/15 11:42:48.041: [amf] INFO: [imsi-001010000000000:1] Release SM context [204] (../src/amf/amf-sm.c:430)
12/15 11:42:48.041: [amf] INFO: [Removed] Number of AMF-Sessions is now 1 (../src/amf/context.c:1847)
12/15 11:42:48.211: [gmm] INFO: [imsi-001010000000000] Registration complete (../src/amf/gmm-sm.c:916)
12/15 11:42:48.211: [amf] INFO: [imsi-001010000000000] Configuration update command (../src/amf/nas-path.c:349)
12/15 11:42:48.211: [gmm] INFO:     UTC [2021-12-15T11:42:48] Timezone[0]/DST[0] (../src/amf/gmm-build.c:508)
12/15 11:42:48.211: [gmm] INFO:     LOCAL [2021-12-15T11:42:48] Timezone[0]/DST[0] (../src/amf/gmm-build.c:513)
12/15 11:42:48.212: [amf] INFO: [Added] Number of AMF-Sessions is now 2 (../src/amf/context.c:1841)
12/15 11:42:48.212: [gmm] INFO: UE SUPI[imsi-001010000000000] DNN[internet] S_NSSAI[SST:1 SD:0xffffff] (../src/amf/gmm-handler.c:821)

# Test user plane connectivity through ping
ip netns exec ue1 ping 8.8.8.8
```

# Monitoring

## Enable monitoring (Prometheus and Grafana) through kube-prometheus-stack
With kube-prometheus we are able to monitor the whole cluster infrasctructure, including nodes, pods, etc. We may use our customized values.yaml.
```bash
# Create monitoring namespace
# Assign monitoring namespace to o5gs-monitoring node if needed (https://stackoverflow.com/questions/52487333/how-to-assign-a-namespace-to-certain-nodes)
kubectl apply -f namespace.yaml

# Step 1: Add repositories
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

# Step 2: Update Helm repositories
helm repo update

# Step 3: Install Prometheus Kubernetes
# - If error on webhooks: follow https://github.com/helm/charts/issues/19928
helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --values values.yaml
helm ls -n monitoring

# Step 4: Grafana UI and Prometheus UI external access through NodePort
# - Then access from GUI (Me.g., MARSAL xDRP)
kubectl apply -f grafana-nodeport-svc.yaml
kubectl apply -f prometheus-nodeport-svc.yaml
```

## Grafana dashboard
Access grafana dashboard through GUI (e.g., through xRDP) via grafana-svc (port 30042) and import dashboard-marsal.json to show the panels of interest for MARSAL.

## Amarisoft SF
In order to monitor the RAN, we may use the Amarisoft API to get info from the Callbox. The file \monitoring\amarisoft-websocket\amarisoft-sf.py contains the script for doing so. By default, the script already exposes metrics to be scraped by Prometheus.

### Adding Amarisoft SF to the cluster
First, we must get the Docker image.
```bash
# Example of Docker image building
docker build -t sbarrachina/amarisoft-websocket:v1.0 .
# Then, push it to the Docker Hub
```
Then, we may update the **helm charts** of the whole Open5GS deployment to include a reference to the created image.

Finally, in order to let Prometheus know where to scrape Amarisoft metrics, we must create the *servicemonitor* \monitoring\amarisoft-websocket\amarisoft-servicemonitor.yaml. If everything worked as expected, you should see Amarisoft as a target of Prometheus in its GUI.