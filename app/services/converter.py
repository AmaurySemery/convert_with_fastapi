import os
import uuid
import subprocess
import asyncio
import logging
from concurrent.futures import ProcessPoolExecutor
from fastapi import UploadFile

from app.services.progress_tracker import set_progress

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

executor = ProcessPoolExecutor(max_workers=4)

def _convert_with_ffmpeg(input_path: str, output_path: str, task_id: str) -> str:
    logger.info(f"[{task_id}] Début conversion avec FFmpeg")
    set_progress(task_id, 50)

    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "128k",
        "-ar", "44100",
        "-y",
        output_path,
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        set_progress(task_id, -1)
        logger.error(f"[{task_id}] Erreur FFmpeg : {result.stderr.decode()}")
        raise RuntimeError(result.stderr.decode())

    set_progress(task_id, 90)
    logger.info(f"[{task_id}] Conversion terminée")
    return output_path

async def convert_video_to_mp3_ffmpeg(file: UploadFile, output_dir: str, task_id: str) -> str:
    logger.info(f"[{task_id}] Début du traitement du fichier : {file.filename}")
    set_progress(task_id, 0)

    original_filename = os.path.basename(file.filename)
    base_name, _ = os.path.splitext(original_filename)

    temp_input = os.path.join(output_dir, f"{uuid.uuid4()}_{original_filename}")
    temp_output = os.path.join(output_dir, f"{base_name}.mp3")

    with open(temp_input, "wb") as f:
        f.write(await file.read())
    logger.info(f"[{task_id}] Fichier temporaire écrit : {temp_input}")

    set_progress(task_id, 20)

    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, _convert_with_ffmpeg, temp_input, temp_output, task_id)

    os.remove(temp_input)
    logger.info(f"[{task_id}] Fichier temporaire supprimé : {temp_input}")

    set_progress(task_id, 100)
    logger.info(f"[{task_id}] Traitement complet du fichier : {file.filename}")
    return temp_output