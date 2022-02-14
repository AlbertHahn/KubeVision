# KubeVision
![alt text](https://github.com/AlbertHahn/KubeVision/blob/main/KubeVision.png)
Logo created in Blender by Albert Hahn.

# Quick Installation with Helm
## Requirements
The local system needs access through kubectl and helm to a running Kubernetes Cluster.
Commands for applying the kubeconfig, export the config as ENV.
`export KUBECONFIG=~/Documents/Kubernetes/KubeVision/kubeconfig_poc`

### Deploying KubeVision through Helm.
`cd helm/flask`
`helm install flask .`

### Necessary step, execute into shell with bash.
`kubectl exec --stdin --tty deploy/mongo -- /bin/bash`

### Run this commands in the deployment pod.
`mongo`
`use admin`
`db.createUser({user: 'admin',pwd: 'password',roles: [ { role: 'root', db: 'admin' } ]})`

The background for this step is that, the mongodb deployment somehow doesn't initialize a admin user on start, needed for CRUD-Operations.

# Quick Deployment with Docker-Compose
## Requirements
Docker and Docker-Compose Installation on the local machine.

### Start Services with Docker-Compose
`cd microservices`
`docker-compose up`