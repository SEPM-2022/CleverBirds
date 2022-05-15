#!/bin/bash
app="clever_birds_e2e_test"

docker stop ${app}
docker rm ${app}
docker rmi ${app}
docker build -f e2e/e2e.Dockerfile -t ${app} e2e/
docker run --name ${app} -d ${app}
docker stop ${app}
docker rm ${app}
