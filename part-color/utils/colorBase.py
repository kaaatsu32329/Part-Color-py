import cv2
import numpy as np
import colorsys

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
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            if mouseData.get_event() == cv2.EVENT_LBUTTONDOWN and click:
                x, y = mouseData.get_pos()
                mask = ColorBase.__correction(self, x, y, image, mask)
                part_color_image = np.where(mask[:,:,np.newaxis], masked_image, gray_image)
                click = 0
            elif mouseData.get_event() == cv2.EVENT_LBUTTONUP:
                click = 1

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
        masked_image = cv2.bitwise_and(image, image, mask)

        return mask, masked_image

    def __correction(self, x, y, image, mask):
        print('{}, {}'.format(x, y))
        h, s, v = ColorBase.get_hsv(image[y, x])
        height, width, _ = image.shape[:3]
        sub_image = image[int(y-height/20) : int(y+height/20), int(x-width/20) : int(x+width/20)]
        sub_hsv = cv2.cvtColor(sub_image, cv2.COLOR_BGR2HSV)
        hsv_min = np.array([h-15, s-25, v-25])
        hsv_max = np.array([h+15, s+25, v+25])
        ground = np.zeros((height, width), dtype=np.uint8)
        if mask[y, x]:
            sub_mask = cv2.inRange(sub_hsv, hsv_min, hsv_max)
            ground[int(y-height/20) : int(y+height/20), int(x-width/20) : int(x+width/20)] = sub_mask
            ground = cv2.bitwise_not(ground)
            new_mask = cv2.bitwise_and(mask, ground)
        else:
            sub_mask = cv2.inRange(sub_hsv, hsv_min, hsv_max)
            ground[int(y-height/20) : int(y+height/20), int(x-width/20) : int(x+width/20)] = sub_mask
            new_mask = cv2.bitwise_or(mask, ground)
        return new_mask

    def get_hsv(color):
        hsv = colorsys.rgb_to_hsv(color[2]/255.0, color[1]/255.0, color[0]/255.0)
        h = int(hsv[0]*180.0)
        s = int(hsv[1]*255.0)
        v = int(hsv[2]*255.0)
        return h, s, v
