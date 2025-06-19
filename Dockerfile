FROM python:3.11-slim

# System dependencies
RUN apt-get update && apt-get install -y git

# Create app directory
WORKDIR /app

# Clone your repo (OR just copy if local)
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
