#!/bin/bash
app="clever_birds"
docker build -t ${app} .
docker run -d -p 80:5000 ${app}
