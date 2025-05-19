# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    ffmpeg \
    libffi-dev \
    build-essential \
    && apt-get clean

# Install Python packages
RUN pip install --no-cache-dir \
    aiohttp \
    hachoir \
    numpy \
    Pillow \
    requests \
    pyrogram \
    tgcrypto \
    olefile \
    motor \
    pytz \
    utils \
    pymongo \
    pyrofork \
    dnspython \
    psutil \
    loggers \
    filetype \
    tldextract \
    ffmpeg-python \
    aiofiles \
    pyromod \
    yt-dlp \
    lk21 \
    pytube \
    flask

# Copy your app code into the container (if needed)
COPY . .

# Default command (you can replace with your script)
CMD ["python3", "bot.py"]
