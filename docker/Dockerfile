FROM alpine:latest

# workaround to install pylint>=2.0.0
RUN apk add --no-cache --update python3-dev py-pip gcc build-base --update bash

COPY ./helixa_app /app/helixa_app
COPY ./categories.json /app/categories.json
COPY ./psychographics.json /app/psychographics.json
COPY ./requirements.txt /app/requirements.txt
COPY ./.bumpversion.cfg /app/.bumpversion.cfg
COPY ./docker/run_helixa_app.sh /app/run_helixa_app.sh

RUN export PYTHONPATH=/app
RUN export PATH=/app:${PATH}
WORKDIR /app
RUN mkdir logs && \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r requirements.txt && \
    chmod +x run_helixa_app.sh

ENTRYPOINT ["./run_helixa_app.sh"]
