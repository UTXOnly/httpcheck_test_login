#!/bin/bash


docker-compose down --remove-orphans
docker stop $(docker ps -a -q)
#Only uncomment if you want REMOVE ALL DOCKER IMAGES!!!
docker rm $(docker ps -a -q) -f
docker rmi $(docker image ls -a -q) -f