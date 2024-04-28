FROM python:3.10.9-slim-buster

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt clean && \
    rm -rf /var/cache/apt/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -U pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /code/app
COPY ./logging.yaml /code/logging.yaml

RUN useradd -m -d /code -s /bin/bash appuser \
    && chown -R appuser:appuser /code/*

WORKDIR /code
USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]