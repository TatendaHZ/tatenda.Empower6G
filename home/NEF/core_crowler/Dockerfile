ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION}-slim AS python-base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update \
    && apt-get install --no-install-suggests --no-install-recommends --yes curl gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv
FROM python-base AS uv-base
ARG UV_VERSION=0.4.10

ENV PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_VERSION=${UV_VERSION}

RUN pip install uv==$UV_VERSION

# Build base with dependencies
FROM uv-base AS build-base

ARG USER=appuser

ENV HOME=/home/${USER}
ENV HF_HOME=${HOME}/.cache/huggingface \
    WORKSPACE=${HOME}/app/

RUN mkdir -p ${WORKSPACE}

WORKDIR ${WORKSPACE}

COPY pyproject.toml requirements.lock ${WORKSPACE}/

RUN uv pip install --no-cache --system -r requirements.lock

# Install Kubernetes Python client
RUN pip install kubernetes

# Copy application source
FROM build-base AS build

ARG PORT=8000
ARG PACKAGE_NAME=core_crowler
ARG USER=appuser
ARG UID=10001

ENV PORT=${PORT} \
    PACKAGE_NAME=${PACKAGE_NAME} \
    HOME=/home/${USER}

# Ensure home directory exists
RUN mkdir -p ${HOME} \
    && useradd -m -d ${HOME} -u ${UID} -s /bin/bash ${USER} \
    && chown -R ${USER}:${USER} ${HOME}

COPY --from=build-base ${WORKSPACE} ${WORKSPACE}
COPY ./src/${PACKAGE_NAME} ${WORKSPACE}/${PACKAGE_NAME}
COPY entrypoint.py ${WORKSPACE}/entrypoint.py
EXPOSE ${PORT}

USER ${USER}

CMD ["python", "-m", "core_crowler.runners.run_loc_crowler"]
