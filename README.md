# Wishes
docker-compose.yaml is the base file to start the project.
Excecute this file using follwing commands:
  docker-compose up --build mysql 
  docker-compose up --build app
  
If we execute above commands two services mysql,app will get started in differnet containers.
see the Docker-compose.yaml

In one container mysql database will be running and in another python3 will be running wih all dependencies.
see the Dockerfile1 and Dockerfile2

These two containers will communicate and send mails to the respective person who has birthday today.
