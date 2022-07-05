# Advanced_Programming_techniques_2022

A demonstration project for the course Advanced_Programming_Techniques_2022
@ECE_Upatras

A) Run localy (Windows)

1. Download the tesseract_location.zip file from here https://www.mediafire.com/file/p32de8mpaeq16mr/tesseract_location.zip/file
2. Export it in your directory of choice . In the same directory add all the .py file besides the example.py and the videocensor.py .
3. In a different directory (or the same) add the example.py and the videocensor.py , pip install all the dependencies (for now) and open the example.py .
   You are set to go, dependencies are :
   Python 3.7+
   uvicorn
   fastapi
   opencv-python
   numpy
   pytesseract
   cdifflib
   requests
   python-multipart
   
B) Run using docker container (Ubuntu using WSL2)

1. Build image (run inside the 'backend' directory)
sudo docker build -t ocr_censor .

2. Run image
sudo docker run -p 8005:8005 ocr_censor

3. Use with CLI (inside the 'frontend' directory)
python3 main.py {filepath} {filename} {words to censor seperated with whitespaces}

