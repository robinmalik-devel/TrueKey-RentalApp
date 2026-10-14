FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
 && apt-get install -y --no-install-recommends binutils gdal-bin libproj-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ARG REQUIREMENTS=dev.txt
COPY requirements/ requirements/
RUN pip install --no-cache-dir -r requirements/${REQUIREMENTS}
COPY . .