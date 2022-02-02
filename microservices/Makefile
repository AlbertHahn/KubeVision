#frontend section
build-frontend:
	cd frontend; \
	docker build -t albird/flask:latest . 

push-frontend:
	cd frontend; \
	docker push albird/flask:latest

build-push-frontend:
	cd frontend; \
	docker build -t albird/flask:latest .; \
	docker push albird/flask:latest

#backend section
build-backend:
	cd frontend; \
	docker build -t albird/flask-opencv:latest . 

push-backend:
	cd frontend; \
	docker push albird/flask-opencv:latest

build-push-backend:
	cd frontend; \
	docker build -t albird/flask-opencv:latest .; \
	docker push albird/flask-opencv:latest