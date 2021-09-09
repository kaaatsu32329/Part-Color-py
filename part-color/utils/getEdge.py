import cv2

class SetEdge():
    def __init__(self, image):
        self.image = image

    def canny(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #gauss_image = cv2.GaussianBlur(gray_image, (3,3), 3)
        #lap_image = cv2.Laplacian(gauss_image, cv2.CV_32F)
        canny_image = cv2.Canny(gray_image, 100, 200)
        return canny_image

    def laplacian(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gauss_image = cv2.GaussianBlur(gray_image, (3,3), 3)
        laplacian_image = cv2.Laplacian(gauss_image, cv2.CV_32F)
        return laplacian_image

    def edging(self, image):
        converted_image = cv2.bitwise_not(image)
        gray_image = cv2.cvtColor(converted_image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contoured_image = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
        return contours