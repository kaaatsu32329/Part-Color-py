import cv2
import numpy as np

def mouse_operation(event, x, y, flags, palam):
    global coord_x, coord_y

    if event == cv2.EVENT_LBUTTONDOWN:
        coord_x = x
        coord_y = y
