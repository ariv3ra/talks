#!/bin/bash
########################################
# Put this on a Server
# run chmod +x deploy_app.sh to make the script executable
#
########################################

echo "Deploying Hello World to Docker Container"
docker stop hello_world
/bin/cp /tmp/hello_world /root/hello_world

echo "Starting Hello World in Docker Container"
docker run -d --rm=true -p 80:5000 -v /root/:/root/ -w /root/ -u root && \
    --name hello_world python:2.7.14 ./hello_world
docker ps -a