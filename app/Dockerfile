FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install curl for the HEALTHCHECK
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

COPY . .

# DELAY_MS is read from .env at runtime (sourced in CMD)

EXPOSE 8000

# HEALTHCHECK: test /health every 10s, timeout 5s, allow 30s start period, 3 retries
HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Start uvicorn, sourcing .env so DELAY_MS is available as an env var
CMD ["sh", "-c", ". /app/.env 2>/dev/null; export DELAY_MS; exec uvicorn main:app --host 0.0.0.0 --port 8000"]