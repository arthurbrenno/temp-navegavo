# Stage 1: Builder
FROM python:3.10-slim-bullseye AS builder

# Set working directory
WORKDIR /app

# Install system dependencies and UV
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && curl -LsSf https://astral.sh/uv/install.sh | sh

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.cargo/bin:$PATH" \
    UV_SYSTEM_PYTHON=1

# Copy only necessary files for dependency installation
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system --no-cache-dir --compile-bytecode -r pyproject.toml

# Stage 2: Runner
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random

# Copy installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

EXPOSE 8000

# Use Uvicorn to run the application
CMD ["uvicorn", "navegavo.asgi:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
