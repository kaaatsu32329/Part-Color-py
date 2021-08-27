import cv2

class MouseOperation():
    def __init__(self, image):
        self.mouseEvent = {'x':None, 'y':None, 'event':None, 'flags':None}
        cv2.setMouseCallback(image, self.__CallBackFunc, None)

    def __CallBackFunc(self, event, x, y, flags, params):
        self.mouseEvent['x'] = x
        self.mouseEvent['y'] = y
        self.mouseEvent['event'] = event
        self.mouseEvent['flags'] = flags

    def getData(self):
        return self.mouseEvent

    def getEvent(self):
        return self.mouseEvent['event']

    def getFlags(self):
        return self.mouseEvent['flags']

    def getPos(self):
        return self.mouseEvent['x'], self.mouseEvent['y']
