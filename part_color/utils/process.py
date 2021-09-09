from utils.selection import Selection
from utils.colorBase import ColorBase
from utils.objectBase import ObjectBase

class Process():
    def __init__(self, proceed):
        self.proceed = proceed

    def run(self):
        selection = Selection()
        colorBase = ColorBase('test')
        objectBase = ObjectBase('test')
        target, object, base = selection.select()

        if base == 'Color':
            color, inverse = selection.select_color()
            if object == 'Image':
                colorBase.image_process(target, color, inverse)
            elif object == 'Movie':
                colorBase.movie_process(target, color, inverse)
            self.proceed = True
        elif base == 'Object':
            object, inverse = selection.selected_object()
            if object == 'Image':
                objectBase.image_process(target, object, inverse)
            elif object == 'Movie':
                objectBase.movie_process(target, object, inverse)
            self.proceed = True
        else:
            print('An error has occured!')
            self.proceed = False
        return self.proceed