FROM python:3.11-slim

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr && apt-get clean

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Expose Flask port
EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python3 -c "import urllib.request; r = urllib.request.urlopen('http://localhost:5000/health'); exit(0) if r.status == 200 else exit(1)"

# Run the app
CMD ["python", "app.py"]
