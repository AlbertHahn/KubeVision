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

### Certs and Secrets are already on the cluster! If not they can be installed with following commands.
`cd helm/certs`\
`kubectl apply -f issuer.yaml`
`kubectl apply -f cert.yaml`
`kubectl apply -f mongodb-secret.yaml`

### Deploying KubeVision through Helm.
`cd helm/kubevision`\
`helm install kubevision .`

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

### Makefile
`cd microservices`\
`make [COMMAND]`\
e.g. `make build-push-facerecognition`

# Build Services locally without docker
Every service directory has a script for exporting enviromental-variables
e.g. flaskStartupFrontend.sh

### Frontend
`cd microservices`\
`cd frontend`\
`source flaskStartupFrontend.sh`\
`flask run --port=8000`

### Facerecognition
`cd microservices`\
`cd facerecognition`\
`source flaskStartupfacerecognition.sh`\
`gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -b 0.0.0.0:5000 run:app`

### Authentication
`cd microservices`\
`cd authentication`\
`source flaskStartupAuth.sh`\
`flask run --port=5001`

### MongoDB needs to be started with docker!
`docker run -p 27017:27017 --name mongodb mongo:4.1.7 `\
`docker exec -it mongodb bash`\
`mongo`\
`use admin`\
`db.createUser({user: 'admin',pwd: 'password',roles: [ { role: 'root', db: 'admin' } ]})`