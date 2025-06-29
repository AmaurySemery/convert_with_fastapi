# Makefile pour FastAPI Video Converter

VENV_NAME := venv
PYTHON := python3
PIP := $(VENV_NAME)/bin/pip
UVICORN := $(VENV_NAME)/bin/uvicorn
APP_PATH := app.main:app

.PHONY: help setup venv install run run-noreload run-watch clean check

help:
	@echo "📌 Commandes disponibles :"
	@echo "  make setup         → Installe python3-venv, pip et ffmpeg"
	@echo "  make venv          → Crée le venv"
	@echo "  make install       → Installe les deps Python"
	@echo "  make run           → Lance FastAPI avec hot-reload standard (⚠️ moviepy)"
	@echo "  make run-noreload  → Lance sans hot-reload (✅ stable)"
	@echo "  make run-watch     → Lance avec watchfiles (✅ recommandé)"
	@echo "  make clean         → Supprime le venv"
	@echo "  make check         → Vérifie env + modules"

setup:
	sudo apt update && sudo apt install -y python3-venv python3-pip ffmpeg

venv:
	$(PYTHON) -m venv $(VENV_NAME)

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	$(UVICORN) $(APP_PATH) --reload

run-noreload:
	$(UVICORN) $(APP_PATH)

run-watch:
	$(UVICORN) $(APP_PATH) --reload --reload-impl watchfiles

clean:
	rm -rf $(VENV_NAME)

check:
	@echo "🔍 Python path: $$(which python)"
	@echo "🔍 Uvicorn path: $$(which $(UVICORN))"
	@echo "🔍 Test import moviepy..."; \
	. $(VENV_NAME)/bin/activate && \
	python -c "from moviepy.video.io.VideoFileClip import VideoFileClip; print('✅ moviepy OK')" || echo "❌ moviepy NOT found"