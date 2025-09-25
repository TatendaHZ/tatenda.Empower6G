# --- Builder image ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git build-essential nodejs npm && rm -rf /var/lib/apt/lists/*

# Clone NEF Emulator repo
RUN git clone https://github.com/medianetlab/NEF_emulator.git . 

# Copy custom .env
COPY env-file-for-local.dev .env

# Prepare dev environment (install Python deps, etc.)
RUN make prepare-dev-env

# --- Runtime image ---
FROM python:3.11-slim

WORKDIR /app

# Install minimal runtime deps
RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
# Copy everything from builder
COPY --from=builder /app /app

# Expose backend port
EXPOSE 8888

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use entrypoint to run backend + db-init at container start
ENTRYPOINT ["/entrypoint.sh"]
