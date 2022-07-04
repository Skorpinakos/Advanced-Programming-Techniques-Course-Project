# API Server

import inspect
from typing import Type
from fastapi import Depends, FastAPI, Form, UploadFile, File
import uvicorn
from pydantic import BaseModel
from pydantic.fields import ModelField
from fastapi.responses import FileResponse
import ocr_service


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

class Params2(BaseModel):
    quality_factor: int
    keywords: list[str]


app = FastAPI()


@ app.post("/receive/", response_model=Params)
async def receive(file: UploadFile = File(...), form: Params = Depends(Params.as_form)):
    contents = await file.read()
    params2 = form.dict()
    list_of_concerns_single = params2['keywords']

    quality_factor = params2['quality_factor']
    file_mode = params2['file_mode']
    check_intervals = params2['check_intervals']
    list_of_concerns_double = []
    for concern in list_of_concerns_single:
        list_of_concerns_double.append([concern, 0.6])

    with open('video_under_procces.mp4', 'wb') as f:
        f.write(contents)
        f.close()

    ocr_service.edit(list_of_concerns_double, 'video_under_procces.mp4',
                     quality_factor, file_mode, check_intervals)
    return FileResponse('store_output_video/video_under_procces.mp4.mp4',  media_type="video/mp4")


@ app.post("/receive_photo/", response_model=Params)
async def receive(file: UploadFile = File(...), form: Params = Depends(Params.as_form)):
    contents = await file.read()
    params2 = form.dict()
    list_of_concerns_single = params2['keywords']

    quality_factor = params2['quality_factor']
    list_of_concerns_double = []
    for concern in list_of_concerns_single:
        list_of_concerns_double.append([concern, 0.6])

    with open('photo_under_procces.png', 'wb') as f:
        f.write(contents)
        f.close()

    ocr_service.edit_photo(list_of_concerns_double, 'photo_under_procces.png',
                     quality_factor)
    return FileResponse('store_output_photo/photo_under_procces.png',  media_type="photo/png")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8002)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8002)
