import cv2
import numpy as np
import sys
import os

args = sys.argv

def main():
    save_dir = './images/'
    image_dir = '../sample_images/'
    target_image = select_image()
    image = cv2.imread(image_dir + target_image)
    h, w, s = image.shape
    image_size = (h, w)

    matrix = np.array([[1, 0, 0], [0, 1, 0]], dtype=np.float32)

    color = select_color()

    mask, masked_image = detect_color(image=image, color=color)

    # Increase saturation of masked image.
    ## masked_image[:,:,(1)] = masked_image[:,:,(1)] * 1.2

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    part_color_image = np.where(mask[:,:,np.newaxis], masked_image, gray_image)

    while True:
        cv2.imshow('Original', image)
        cv2.imshow('Part color', part_color_image)
        ## cv2.imshow('Mask', mask)
        ## cv2.imshow('Masked', masked_image)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # CAUTION! The file name is already exist!!!
    ## cv2.imwrite(save_dir + 'shrine_red.jpg', part_color_image)

    cv2.destroyAllWindows()

def detect_color(image, color):
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

    # Masking processing
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return mask, masked_image

def select_image():
    dir_images = '../samples/'
    list_images = os.listdir(dir_images)
    print(list_images)
    target_image = input('Which image do you want to process? -> ')
    target_image = str(target_image)
    return target_image

def select_color():
    print('Which color will you use?')
    selected = input('red, green, blue -> ')
    selected = str(selected)
    return selected

if __name__ == "__main__":
    main()