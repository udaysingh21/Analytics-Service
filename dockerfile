# ----------------------------
# Stage 1 — Build dependencies
# ----------------------------
FROM python:3.10-slim AS builder

# Avoid python buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /app

# Install system packages for building Python deps (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install dependencies to a temporary folder
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt


# ----------------------------
# Stage 2 — Final Runtime Image
# ----------------------------
FROM python:3.10-slim

WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy your application code
COPY . .

# Expose service port
EXPOSE 8005

# Start the service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8005"]
