ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.20

FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip

COPY requirements.txt /

RUN pip3 install --no-cache-dir --break-system-packages -r /requirements.txt

COPY . /

RUN chmod a+x /run.sh

CMD ["/run.sh"]