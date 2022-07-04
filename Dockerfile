FROM ubuntu:22.04
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    python3 \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

# Python version
FROM python:3.10

# Scripts
ADD api_controller.py .
ADD ocr_service.py .
ADD compose.py .
ADD detect.py .
ADD split.py .
ADD videocensor.py .

# Dependencies
RUN pip install typing
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install pydantic
RUN pip install numpy
RUN pip install opencv-python
RUN pip install requests
RUN pip install numpy
RUN pip install pytesseract
RUN pip install detect
RUN pip install compose
RUN pip install split

ENTRYPOINT ["python","./main.py"]


