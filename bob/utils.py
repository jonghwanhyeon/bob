import cv2
import numpy as np
import requests


def fetch_image(url):
    response = requests.get(url)
    content = np.frombuffer(response.content, dtype=np.uint8)
    image = cv2.imdecode(content, cv2.IMREAD_COLOR)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def to_png(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    content = cv2.imencode('.png', image)[1]
    return content