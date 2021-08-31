import cv2
import numpy as np

from utils.operation import MouseOperation

class ColorBase():
    def __init__(self, path):
        self.path = path

    def image_process(self, target, color, inverse):
        IMAGE_DIR = '../sample_images/'
        image = cv2.imread(IMAGE_DIR + target)
        cv2.namedWindow('Original')
        cv2.namedWindow('Part color')
        mouseData = MouseOperation('Part color')
        click = 1

        mask, masked_image = ColorBase.detect_color(self, image=image, color=color, inverse=inverse)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

        part_color_image = np.where(mask[:,:,np.newaxis], masked_image, gray_image)

        while True:
            cv2.imshow('Original', image)
            cv2.imshow('Part color', part_color_image)

            cv2.waitKey(1)
            #key = cv2.waitKey(1)
            #if key == ord('q'):
            #    break
            if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN and click:
                x, y = mouseData.getPos()
                ColorBase.__correction(self, x, y)
                click = 0
            elif mouseData.get_event() == cv2.EVENT_LBUTTONUP:
                click = 1
            elif mouseData.get_event() == cv2.EVENT_RBUTTONDOWN:
                break

        cv2.destroyAllWindows()

    def movie_process(self, target, color, inverse):
        MOVIE_DIR = '../sample_movies/'
        movie = cv2.VideoCapture(MOVIE_DIR + target)

        playback, frame = movie.read()

        height, width, _ = frame.shape
        fps = movie.get(cv2.CAP_PROP_FPS)
        #player = cv2.VideoWriter('./images/partcolor.mp4', cv2.VideoWriter_fourcc('m','p','4','v'), fps, (width, height), True)

        cv2.namedWindow('Original')
        cv2.namedWindow('Part color')

        while playback:
            mask, masked_frame = ColorBase.detect_color(self, image=frame, color=color, inverse=inverse)

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

            part_color_frame = np.where(mask[:,:,np.newaxis], masked_frame, gray_frame)

            cv2.imshow('Original', frame)
            cv2.imshow('Part color', part_color_frame)

            #player.write(part_color_frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

            playback, frame = movie.read()

        movie.release()
        #player.release()
        cv2.destroyAllWindows()

    def detect_color(self, image, color, inverse):
        # Convert to HSV space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        if color == 'red':
            # Range of red color in HSV 1
            hsv_min = np.array([0,64,0])
            hsv_max = np.array([10,255,255])
            mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

            # Range of red color in HSV 1
            hsv_min = np.array([170,64,0])
            hsv_max = np.array([179,255,255])
            mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

            # Mask of red colors domain (255: red, 0: else)
            mask = mask1 + mask2

        elif color == 'green':
            # Range of green color in HSV
            hsv_min = np.array([30, 64, 0])
            hsv_max = np.array([90,255,255])

            # Mask of green colors domain (255: green, 0: else)
            mask = cv2.inRange(hsv, hsv_min, hsv_max)

        elif color == 'blue':
            # Range of blue color in HSV
            hsv_min = np.array([90, 64, 0])
            hsv_max = np.array([150,255,255])

            # Mask of blue colors domain (255: blue, 0: else)
            mask = cv2.inRange(hsv, hsv_min, hsv_max)

        elif color == 'orange':
            # Range of orange color in HSV
            hsv_min = np.array([16,100,150])
            hsv_max = np.array([44,255,255])

            # Mask of orange colors domain (255: blue, 0: else)
            mask = cv2.inRange(hsv, hsv_min, hsv_max)

        else:
            pass

        if inverse:
            mask = cv2.bitwise_not(mask)

        # Masking processing
        masked_image = cv2.bitwise_and(image, image, mask=mask)

        return mask, masked_image

    def __correction(self, x, y):
        print('{}, {}'.format(x, y))
