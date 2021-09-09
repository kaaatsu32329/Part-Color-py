from typing import Set
import cv2
import numpy as np
import os

from utils.operation import MouseOperation

class Changer():
    def __init__(self):
        self.target = ''
        self.component = ''
        self.increment = True

    def changer(self):
        target = Changer.get_image(self)
        IMAGE_DIR = '../sample_images/'
        image = cv2.imread(IMAGE_DIR + target)
        cv2.namedWindow('Original' ,cv2.WINDOW_NORMAL)
        cv2.namedWindow('Changer', cv2.WINDOW_NORMAL)
        mouseData = MouseOperation('Changer')
        click = 1
        changed_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        cv2.imshow('Original', image)
        cv2.imshow('Changer', changed_image)

        while True:
            delta = Changer.select(self)

            changed_image[:,:,(0)] = changed_image[:,:,(0)] + delta[0]
            changed_image[:,:,(1)] = changed_image[:,:,(1)] * delta[1]
            changed_image[:,:,(2)] = changed_image[:,:,(2)] * delta[2]

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            if mouseData.get_event() == cv2.EVENT_LBUTTONDOWN and click:
                x, y = mouseData.get_pos()
                click = 0
            elif mouseData.get_event() == cv2.EVENT_LBUTTONUP:
                click = 1

            changed_image = cv2.cvtColor(changed_image, cv2.COLOR_HLS2BGR)

            cv2.imshow('Original', image)
            cv2.imshow('Changer', changed_image)

        cv2.destroyAllWindows()

    def get_image(self):
        DIR = '../sample_images/'
        list_datas = os.listdir(DIR)
        print(list_datas)
        image_selecting = True
        while image_selecting:
            self.target = input('Which do you want to process? >> ')
            self.target = str(self.target)
            image_selecting = not os.path.isfile(DIR + self.target)
        return self.target

    def select(self):
        self.component = input('[h]ue or [s]aturation or [v]alue >> ')
        self.increment = input('[u]p or [d]own >> ')
        self.increment = True if self.increment=='u' or self.increment=='up' else False
        if self.component == 'h' or self.component == 'hue':
            if self.increment:
                changer = np.array([60, 0, 0])
            else:
                changer = np.array([-60, 0, 0])
        elif self.component == 's' or self.component == 'saturation':
            if self.increment:
                changer = np.array([0, 1.2, 0])
            else:
                changer = np.array([0, 0.8, 0])
        elif self.component == 'v' or self.component == 'value':
            if self.increment:
                changer = np.array([0, 0, 1.2])
            else:
                changer = np.array([0, 0, 0.8])
        else:
            changer = np.array([0, 0, 0])
        return changer
