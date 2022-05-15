#!/bin/bash
app="clever_birds_e2e_test"

docker stop ${app}
docker rm ${app}
docker rmi ${app}
docker run --name ${app} -it -v $PWD/e2e:/e2e -w /e2e -e CYPRESS_baseUrl=http://host.docker.internal cypress/included:9.4.1
docker stop ${app}
docker rm ${app}
