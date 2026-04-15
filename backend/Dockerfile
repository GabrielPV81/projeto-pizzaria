# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# cria usuário
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# instala dependências (VERSÃO SIMPLES)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia código
COPY . .

# usa usuário
USER appuser

EXPOSE 8000

CMD ["python", "app.py"]
