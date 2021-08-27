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