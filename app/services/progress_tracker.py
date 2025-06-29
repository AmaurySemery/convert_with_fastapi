from typing import Dict
from threading import Lock
import logging

logging.basicConfig(level=logging.INFO)

_progress: Dict[str, int] = {}
_lock = Lock()

def set_progress(task_id: str, percent: int):
    with _lock:
        _progress[task_id] = percent
        logging.info(f"Progress for {task_id}: {percent}%")

def get_progress(task_id: str) -> int:
    with _lock:
        return _progress.get(task_id, 0)