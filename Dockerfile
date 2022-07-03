# Python version
FROM python:3

# Scripts
ADD api_controller.py /
ADD ocrservice.py /
ADD compose.py /
ADD detect.py /
ADD split.py /
ADD videocensor.py /

# Dependencies
RUN pip install inspect
RUN pip install typing
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install pydantic
RUN pip install cv2
RUN pip install os
RUN pip install shutil
RUN pip install subprocess
RUN pip install requests
RUN pip install numpy
RUN pip install pytesseract
RUN pip install difflib
RUN pip install detect
RUN pip install compose
RUN pip install split

CMD ["python","start.py","(api-url) ","(api-key)","(file-path)"]


