FROM python:3.10-slim

ENV APP_HOME="/user/service"
ENV PYTHONPATH=${APP_HOME}
ENV APP_WORKER_COUNT=1

RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}

ADD requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt  && \
	rm -rf /root/.cache/pip

COPY . ${APP_HOME}

ENTRYPOINT ["/user/service/docker-entrypoint.sh"]
