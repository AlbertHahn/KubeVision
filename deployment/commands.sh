kubectl label nodes microservice0 hardware=cloud
kubectl label nodes microservice1 hardware=cloud
kubectl label nodes microservice2 hardware=premise

kubectl taint nodes microservice2 hardware=cpu:NoSchedule