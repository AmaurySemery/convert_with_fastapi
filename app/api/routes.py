from fastapi import APIRouter, UploadFile, File
from typing import List
from app.services.converter import convert_video_to_mp3_ffmpeg
from app.services.progress_tracker import get_progress
import os
import uuid

router = APIRouter()

@router.post("/convert/")
async def upload_and_convert(files: List[UploadFile] = File(...)):
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    result_files = []

    for file in files:
        task_id = str(uuid.uuid4())
        mp3_path = await convert_video_to_mp3_ffmpeg(file, output_dir, task_id)
        filename = os.path.basename(mp3_path)
        size = os.path.getsize(mp3_path)
        result_files.append({
            "task_id": task_id,
            "filename": filename,
            "size_bytes": size,
            "progress": get_progress(task_id)
        })

    return {"converted_files": result_files}

@router.get("/progress/{task_id}")
def get_conversion_progress(task_id: str):
    return {
        "task_id": task_id,
        "progress": get_progress(task_id)
    }