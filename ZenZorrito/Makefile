# Makefile for Python project

# Variables
PYTHON = python3
PIP = pip
SRC_DIR = src
DATA_DIR = data
TEST_DIR = tests

# Tareas
run:
	$(PYTHON) $(SRC_DIR)/main.py $(DATA_DIR)/sample.csv

install:
	$(PIP) install -r requirements.txt

clean:
	rm -rf venv __pycache__

.PHONY: run install clean
