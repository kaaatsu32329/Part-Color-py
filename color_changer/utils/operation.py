import cv2

class MouseOperation():
    def __init__(self, image):
        self.mouseEvent = {'x':None, 'y':None, 'event':None, 'flags':None}
        cv2.setMouseCallback(image, self.__call_back_func, None)

    def __call_back_func(self, event, x, y, flags, params):
        self.mouseEvent['x'] = x
        self.mouseEvent['y'] = y
        self.mouseEvent['event'] = event
        self.mouseEvent['flags'] = flags

    def get_data(self):
        return self.mouseEvent

    def get_event(self):
        return self.mouseEvent['event']

    def get_flags(self):
        return self.mouseEvent['flags']

    def get_pos(self):
        return self.mouseEvent['x'], self.mouseEvent['y']
