# API Server

import inspect
from typing import List, Tuple, Type
from fastapi import Depends, FastAPI, Form, Request, UploadFile, File
import uvicorn
from pydantic import BaseModel
from pydantic.fields import ModelField
from fastapi.responses import FileResponse
import json


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


class Keyword(BaseModel):
    keyword: str
    matching_level: float


@as_form
class Params(BaseModel):
    quality_factor: int
    file_mode: str
    check_intervals: int
    keywords: list[str]


app = FastAPI()


@ app.post("/receive/", response_model=Params)
async def receive(file: UploadFile = File(...), form: Params = Depends(Params.as_form)):
    return FileResponse('store_output_video/video_under_procces.mp4',  media_type="video/mp4")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
