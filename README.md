# 🎵 Convert With FastAPI

Une mini-application FastAPI qui permet d’uploader une ou plusieurs vidéos, de les convertir en fichiers MP3 via `ffmpeg`, et de suivre la progression de chaque tâche.

---

## 🚀 Fonctionnalités

- 📤 Upload de vidéos (supporte les uploads multiples)
- 🔄 Conversion en `.mp3` avec `ffmpeg`
- ⚙️ Traitement asynchrone avec `asyncio` et `ProcessPoolExecutor`
- 📈 Suivi de la progression pour chaque tâche (`/progress/{task_id}`)
- 🧾 Interface Swagger intégrée (`/docs`)

---

## 📂 Structure du projet

```
convert_with_fastapi/
│
├── app/
│   ├── api/
│   │   └── routes.py           # Définition des endpoints
│   ├── services/
│   │   ├── converter.py        # Logique de conversion
│   │   └── progress_tracker.py # Suivi des tâches
│   └── uploads/                # Répertoire des fichiers temporaires (à ignorer)
│
├── main.py                     # Point d’entrée FastAPI
├── requirements.txt            # Dépendances
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

1. **Cloner le repo :**

```bash
git clone https://github.com/AmaurySemery/convert_with_fastapi.git
cd convert_with_fastapi
```

2. **Créer un environnement virtuel :**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Installer les dépendances :**

```bash
pip install -r requirements.txt
```

---

## ▶️ Lancer le serveur

```bash
uvicorn main:app --reload
```

Visite ensuite [http://localhost:8000/docs](http://localhost:8000/docs) pour interagir avec l’API.

---

## 🧪 Endpoints utiles

- `POST /upload`: Upload et conversion d’un ou plusieurs fichiers
- `GET /progress/{task_id}`: Récupération de la progression d’une tâche

---

## 💬 Exemple d’usage

1. Envoie une vidéo via `/upload` (dans Swagger ou Postman).
2. Récupère l’`id` de tâche retourné.
3. Interroge `/progress/{task_id}` pour voir l’avancement.
4. Une fois terminé (100%), le fichier `.mp3` est prêt dans `uploads/`.

---

## 🧹 .gitignore recommandé

```gitignore
venv/
uploads/
*.mkv
*.mp4
*.avi
*.mov
*.flac
*.ogg
*.webm
```

---

## 🧱 Notes techniques

- Utilise `ProcessPoolExecutor` pour paralléliser les conversions.
- Les logs de progression sont affichés dans la console avec `logging`.
- `progress_tracker.py` utilise un `threading.Lock` pour garantir la sécurité des données partagées.

---

## 🧤 Limitations et TODO

- ❌ Pas encore d’interface HTML utilisateur (frontend minimaliste à venir ?)
- ❌ Pas de reprise de conversion après échec

---

## 📜 Licence

Ce projet est open-source et libre d’utilisation dans le cadre d’un usage personnel ou professionnel.

---

## 🧠 Auteur

Amaury Semery – développeur