# Use Python 3.10 slim as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for Scrapy
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    libxml2 \
    libxslt1-dev \
    zlib1g-dev \
    libjpeg-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Ensure Pip is installed and upgraded
RUN python -m ensurepip && pip install --upgrade pip setuptools wheel

# **Copy the requirements file BEFORE installing dependencies**
COPY requirements.txt /app/requirements.txt

# **Print debugging information to verify requirements.txt**
RUN echo "Checking if requirements.txt is copied:" && ls -l /app/requirements.txt || echo "File missing!"
RUN cat /app/requirements.txt || echo "File is empty!"

# **Install dependencies, including Scrapy**
RUN pip install --no-cache-dir -r /app/requirements.txt

# **Copy the entire Scrapy project into the container**
COPY . /app

# **Ensure Scrapy is available in PATH**
ENV PATH="/root/.local/bin:$PATH"

# **Set default command to keep the container running**
CMD ["tail", "-f", "/dev/null"]

