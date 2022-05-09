#!/bin/bash
app="clever_birds_test"
game="clever_birds_game_test"
docker stop ${app}
docker stop ${game}
docker rm ${app}
docker rm ${game}
docker rmi ${app}
docker rmi ${game}
docker build -f static/js/game/dockerfiles/test.Dockerfile -t ${game} static/js/game/
docker run --name ${game} -d ${game}
docker stop ${game}
docker rm ${game}

docker build . -t python_test
docker run -it --entrypoint "/usr/bin/env" python_test /usr/local/bin/python tests.py
