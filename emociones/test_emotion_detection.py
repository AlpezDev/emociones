import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response['dominant_emotion'], 'joy')

    def test_anger(self):
        response = emotion_detector("I am really mad about this")
        self.assertEqual(response['dominant_emotion'], 'anger')

    def test_sadness(self):
        response = emotion_detector("I feel sad")
        self.assertEqual(response['dominant_emotion'], 'sadness')

if __name__ == "__main__":
    unittest.main()