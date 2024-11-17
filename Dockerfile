FROM alpine:3.14

RUN apk add --no-cache python3 py3-pip gcc musl-dev python3-dev

WORKDIR /app

COPY sum.py .

# Créer un environnement virtuel
RUN python3 -m venv venv

# Activer l'environnement virtuel et installer les packages
RUN . venv/bin/activate && \
    pip install --no-cache-dir --upgrade pip setuptools wheel sphinx

CMD ["tail", "-f", "/dev/null"]
