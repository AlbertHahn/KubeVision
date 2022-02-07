kubectl label nodes microservice0 hardware=cloud
kubectl label nodes microservice1 hardware=cloud
kubectl label nodes microservice2 hardware=premise

kubectl taint nodes microservice2 hardware=cpu:NoSchedule

mongo --host mongodbservice --port 27017 -u admin -p password --authenticationDatabase admin

MongoClient("mongodb://admin:password@mongodbservice:27017/?authSource=admin")

use admin
db.addUser("admin", "password", true)

db.user.insert({name: "admin", password: "password"})



mongo
use admin

db.createUser({user: 'admin',pwd: 'password',roles: [ { role: 'root', db: 'admin' } ]})


use total_records
db.user.insert({"name":"test", 'password': "test"})