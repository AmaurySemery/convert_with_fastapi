import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')
TEMP_DIR = os.path.join(BASE_DIR, 'temp')

SUPPORTED_FORMATS = ('.mp4', '.mkv')

# Création des répertoires au lancement
for path in [UPLOAD_DIR, OUTPUT_DIR, TEMP_DIR]:
    os.makedirs(path, exist_ok=True)