# KubeVision
![alt text](https://github.com/AlbertHahn/KubeVision/blob/main/KubeVision.png)
Logo created in Blender by Albert Hahn.

KubeVision is a microservice web-application, developed for my bachelor thesis.
The application provides a GUI and allows the user to authenticate through either password and username or face-detection.


# Online Kubernetes Deployment with Helm
## Requirements
The local system needs access through kubectl and helm to a running Kubernetes Cluster.
Commands for applying the kubeconfig, export the config as ENV.

`export KUBECONFIG=~/your/path/to/KubeVision/kubeconfig_poc`

### Deploying KubeVision through Helm.
`cd helm/flask`\
`helm install flask .`

### Necessary step, execute into shell with bash.
`kubectl exec --stdin --tty deploy/mongo -- /bin/bash`\

### Run this commands in the deployment pod.
`mongo`\
`use admin`\
`db.createUser({user: 'admin',pwd: 'password',roles: [ { role: 'root', db: 'admin' } ]})`

The background for this step is that, the mongodb deployment somehow doesn't initialize a admin user on start, needed for CRUD-Operations.

# Offline Deployment with Docker-Compose
## Requirements
Docker and Docker-Compose Installation on the local machine.

### Start Services with Docker-Compose
`cd microservices`\
`docker-compose up`