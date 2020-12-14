FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV SERVICE_NAME "fast-api-purser"
ENV USER_HOME "/opt/$SERVICE_NAME"
ENV APP_PATH "$USER_HOME/application"
ENV WEB_PORT 8888


RUN set -ex && \
    mkdir -p  $USER_HOME


COPY ./  $USER_HOME


WORKDIR $USER_HOME


RUN set -ex && \
    pip install poetry && \
    poetry install -n


WORKDIR APP_PATH


# Run FastApi
CMD [ "sh", "-c", "uvicorn ${APP_HOME}/server/app:app --http_host=0.0.0.0 --http_port=${WEB_PORT}"]
