import ocr_service
import uvicorn
from fastapi import File, UploadFile, FastAPI
from fastapi.responses import FileResponse
import os

list_of_concerns = [['ΙΩΑ', 0.6], ['ΙΩΑΝΝΗΣ', 0.6], ['ΤΣΑΜΠΡΑΣ', 0.6], ['ΣΤΑΜΑΤΙΟΥ', 0.75], [
    'ΙΩΑΝΝΗΣΤΣΑΜΠΡΑΣ', 0.6], ["up1066584", 0.5]]  # choose keywords and sensitivity
video_name = "directory/test.mp4"  # choose input video location
quality_factor = 1
file_mode = 'file'
check_intervals = 30  # fps

app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        print('step1')
        with open('video_under_procces.mp4', 'wb') as f:
            f.write(contents)
            f.close()
        print('step1')
        try:
            ocr_service.edit(list_of_concerns, 'video_under_procces.mp4',
                             quality_factor, file_mode, check_intervals)
        except Exception as error_name:
            print(error_name)
        print('step1')
        os.remove('video_under_procces.mp4')
        print('step1')

    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()

    # time.sleep(1)
    response_dict = {'authors': 'tsampras & kanias'}
    return FileResponse('store_output_video/video_under_procces.mp4', headers=response_dict, media_type="video/mp4")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
