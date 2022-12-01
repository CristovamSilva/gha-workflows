# syntax=docker/dockerfile:1
FROM python:3.10 as base

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    <<eot bash
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get -y upgrade
apt-get -y install --no-install-recommends build-essential gcc
apt-get clean
mkdir -p -m 0600 /root/.ssh &&
ssh-keyscan -H github.com >> /root/.ssh/known_hosts
rm -rf /var/lib/apt/lists/*
eot

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY . .
RUN --mount=type=cache,target=/root/.cache/pip pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim

COPY --from=base /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY app app

CMD [ "python", "-m", "app" ]
