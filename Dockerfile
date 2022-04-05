FROM python:3-alpine3.10 AS base

RUN mkdir /install
WORKDIR /install

RUN apk add build-base

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

ENV FLASK_APP app.py
WORKDIR /project
COPY --from=base /install /usr/local
ADD . /project

EXPOSE 5000

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]