from fastapi import FastAPI, UploadFile, Form, HTTPException
import shutil
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import cv2 as cv
import sys

a = sys.path.append('./modules/')

import pickDir

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:4000"],
)

@app.get('/data')
async def get_data():
    return {'body': 'hello'}

@app.post('/arquivo')
async def post_arquivo(arquivo: List[UploadFile]):
    for img in arquivo:
        with open(f'./input/{img.filename}', "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {"file_name": "Good"}

@app.post('/preparedImage')
async def preparedImage(dirName: str):
    await pickDir.pickDir(dirName)
    return {"file_name": "Good"}

def start():
    uvicorn.run("app:app", host='localhost', port=8080, reload=True)

if __name__ == '__main__':
    start()
