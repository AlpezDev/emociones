# Final Project

## Emotion Detection Web Application

This project is a web-based emotion detection application built using Watson NLP. The application can detect the following emotions from text input:

- Anger
- Disgust
- Fear
- Joy
- Sadness

It also identifies the **dominant emotion**.

### Technologies Used
- Python 3.x
- Flask
- Requests
- Watson NLP API

### Usage
Import the `emotion_detector` function from the package and call it with text input:

```python
from EmotionDetection.emotion_detection import emotion_detector

result = emotion_detector("I am happy")
print(result)
