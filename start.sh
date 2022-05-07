#!/bin/bash
app="clever_birds"
game="clever_birds_game"
docker stop ${app}
docker stop ${game}
docker rm ${app}
docker rm ${game}
docker rmi ${app}
docker rmi ${game}
docker build -t ${app} .
docker run --name ${app} -v $PWD:/project -d -p 80:5000 ${app}
docker build -f static/js/game/dockerfiles/build.Dockerfile -t ${game} static/js/game/
docker run --name ${game} -d -p 8080:80 ${game}
