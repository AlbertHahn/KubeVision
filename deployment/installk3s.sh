#!/bin/sh
ip4=$(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1)
COUNTER=1
NODECOUNT=0
PREFIX=""
HOSTNAMES=""
HOSTS=""

MYCLUSTERNAME="cvcluster"

echo "How many nodes do you want to deploy?"
read NODECOUNT

echo "Which prefix should be used for your nodes?"
read PREFIX

for i in $(seq 1 $NODECOUNT); do 
    HOSTNAMES+=("$PREFIX""$i")
    echo "Enter IP for node $PREFIX$i"
    read HOSTS[$i]
done

hostnamectl set-hostname "$PREFIX"0


curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION={v1.20.4+k3s1} INSTALL_K3S_EXEC="server" K3S_CLUSTER_INIT=1 sh -
TOKEN=$( cat /var/lib/rancher/k3s/server/node-token )

USERNAME=root
SCRIPT="curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION={v1.20.4+k3s1} INSTALL_K3S_EXEC="server" K3S_TOKEN=$TOKEN K3S_URL=https://$ip4:6443 sh - "
for HOSTNAME in ${HOSTS[@]} ; do
    ssh -o StrictHostKeyChecking=no -l ${USERNAME} ${HOSTNAME} "hostnamectl set-hostname ${HOSTNAMES[$COUNTER]}; ${SCRIPT}"  
    echo "HOSTNAME CHANGED: ${HOSTNAMES[$COUNTER]}"
    ((COUNTER++))
done

curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3

chmod 700 get_helm.sh

./get_helm.sh

echo "waiting for helm-install-traefik 50s"
sleep 50
kubectl get jobs -n kube-system
echo "finished"

export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

helm repo add rancher-latest https://releases.rancher.com/server-charts/latest

helm search repo rancher

kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v1.0.4/cert-manager.crds.yaml

kubectl create namespace cert-manager

helm repo add jetstack https://charts.jetstack.io

kubectl create namespace cattle-system

helm install \
cert-manager jetstack/cert-manager \
--namespace cert-manager \
--version v1.0.4

echo "Job finished, the cluster has been successfully initialized"