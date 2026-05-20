FROM python:3.11-slim

# System packages
RUN apt-get update && apt-get install -y \
    git \
    curl \
    ffmpeg \
    aria2 \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Work directory
WORKDIR /workspace

# Copy requirements first
COPY requirements.txt .

# Upgrade pip tools
RUN pip install --upgrade pip setuptools wheel

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Start bot
CMD ["bash", "start.sh"]
