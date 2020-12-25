import cv2
import numpy as np

from bob import logic
from dictlogic import Primitive, builtins

@logic.add('blur')
def blur(std):
    image = builtins['get'](Primitive('image'))
    image = cv2.GaussianBlur(image, (0, 0), std())
    builtins['set'](Primitive('image'), Primitive(image))
    return image

@logic.add('tint')
def tint(red, blue, green, alpha):
    image = builtins['get'](Primitive('image'))
    height, width = image.shape[:2]
    overlay = np.tile([red(), blue(), green()], [height, width, 1]).astype(np.uint8)
    image = cv2.addWeighted(image, (1 - alpha()), overlay, alpha(), 0)
    builtins['set'](Primitive('image'), Primitive(image))
    return image

@logic.add('representative')
def representative():
    image = builtins['get'](Primitive('image'))
    return np.mean(image.reshape(-1, 3), axis=0).astype(np.uint8)

@logic.add('to_hsl')
def to_hsl(rgb):
    return cv2.cvtColor(np.array([[rgb()]]).astype(np.uint8), cv2.COLOR_RGB2HSV)[0][0][[0, 2, 1]]

@logic.add('to_hsv')
def to_hsv(rgb):
    return cv2.cvtColor(np.array([[rgb()]]).astype(np.uint8), cv2.COLOR_RGB2HSV)[0][0]