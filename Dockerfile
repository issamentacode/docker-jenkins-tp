FROM alpine:3.14

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        python3-dev \
    && apk add --no-cache python3 py3-pip

WORKDIR /app

COPY sum.py .

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir sphinx

CMD ["tail", "-f", "/dev/null"]
