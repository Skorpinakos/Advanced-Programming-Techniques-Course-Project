# Python 3.10 on debian bullseye
FROM python:3.10-bullseye

# Install the tesseract-ocr package
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y tesseract-ocr tesseract-ocr-ell \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Scripts
COPY . .
CMD ["python3", "./api_controller.py"]

# Server runs on port 8002
EXPOSE 8005
