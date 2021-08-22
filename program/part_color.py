import cv2
import numpy as np

def main():
    image = cv2.imread('./images/shrine.jpg')

    color = 'red'

    _, masked_image = detect_color(image=image, color=color)

    # Increase saturation of masked image.
    masked_image[:,:,(1)] = masked_image[:,:,(1)] * 1.2

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    part_color_image = cv2.add(masked_image, gray_image)
    #part_color_image2 = cv2.bitwise_or(masked_image, gray_image)

    while True:
        cv2.imshow('Original', image)
        #cv2.imshow('Masked', masked_image)
        cv2.imshow('Part color', part_color_image)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

def detect_color(image, color):
    # Convert to HSV space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    if color == 'red':
        # Range of red color in HSV 1
        hsv_min = np.array([0,64,0])
        hsv_max = np.array([30,255,255])
        mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

        # Range of red color in HSV 1
        hsv_min = np.array([150,64,0])
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

if __name__ == "__main__":
    main()