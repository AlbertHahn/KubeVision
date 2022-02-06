docker run --name auth-service \
      -e homeEndpoint=localhost:5000/ \
      -e trainEndpoint=localhost:5000/train \
      -e mongoEndpoint=mongodb://admin:password@localhost:27017/ \
      -p 5001:5001 \
      albird/flask-auth:latest



      