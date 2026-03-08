# Emotion Detector – AI Web Application

## Descripción
Este proyecto implementa una aplicación web de detección de emociones utilizando Python y la biblioteca Watson NLP, la aplicación analiza texto ingresado por el usuario y devuelve las emociones detectadas, junto con la emoción dominante.

El sistema fue desarrollado como parte del proyecto final del curso de desarrollo con Python.

## Tecnologías utilizadas
- Python
- Flask
- Watson NLP API
- Requests
- PyLint
- Unittest

## Funcionalidades
- Analiza texto para detectar emociones.
- Devuelve valores de:
  - anger
  - disgust
  - fear
  - joy
  - sadness
- Identifica la emoción dominante.
- Interfaz web mediante Flask.
- Manejo de errores cuando el usuario no introduce texto.
- Pruebas unitarias incluidas.
- Análisis de calidad de código con PyLint.

## Estructura del proyecto
EmotionDetection/
│
├── init.py
├── emotion_detection.py
│
tests/
├── test_emotion_detection.py
│
server.py
README.md
