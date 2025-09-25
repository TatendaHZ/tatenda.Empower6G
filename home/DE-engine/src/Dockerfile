FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source

# Expose DE port
EXPOSE 10020

# Run API
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "10020"]
