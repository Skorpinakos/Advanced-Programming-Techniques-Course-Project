import ocr_service
import uvicorn
from fastapi import File, UploadFile, FastAPI, Form, Depends
from fastapi.responses import FileResponse
import os
from pydantic import BaseModel
from pydantic.fields import ModelField
from typing import Type
import inspect
import random

list_of_concerns = [['ΙΩΑ', 0.6], ['ΙΩΑΝΝΗΣ', 0.6], ['ΤΣΑΜΠΡΑΣ', 0.6], ['ΣΤΑΜΑΤΙΟΥ', 0.75], [
    'ΙΩΑΝΝΗΣΤΣΑΜΠΡΑΣ', 0.6], ["up1066584", 0.5]]  # choose keywords and sensitivity
video_name = "directory/test.mp4"  # choose input video location
quality_factor = 1
file_mode = 'file'
check_intervals = 30  # fps


def as_form(cls: Type[BaseModel]):
    new_parameters = []

    for field_name, model_field in cls.__fields__.items():
        model_field: ModelField  # type: ignore

        new_parameters.append(
            inspect.Parameter(
                model_field.alias,
                inspect.Parameter.POSITIONAL_ONLY,
                default=Form(...) if not model_field.required else Form(
                    model_field.default),
                annotation=model_field.outer_type_,
            )
        )

    async def as_form_func(**data):
        return cls(**data)

    sig = inspect.signature(as_form_func)
    sig = sig.replace(parameters=new_parameters)
    as_form_func.__signature__ = sig  # type: ignore
    setattr(cls, 'as_form', as_form_func)
    return cls


@as_form
class Params(BaseModel):
    quality_factor: int
    file_mode: str
    check_intervals: int
    keywords: list[str]


app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile = File(...), form: Params = Depends(Params.as_form)):
    try:
        contents = await file.read()
        params = await form.dict()
        print('step1')
        with open('video_under_procces.mp4', 'wb') as f:
            f.write(contents)
            f.close()
        print('step1')
        list_of_concerns = []
        for i in range(len(params['keywords'])):
            list_of_concerns[i] = (params['keywords'][i], random.random())
        try:
            ocr_service.edit(list_of_concerns, 'video_under_procces.mp4',
                             params['quality_factor'], params['file_mode'], params['check_intervals'])
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
