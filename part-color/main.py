import sys
from utils.selection import Selection
from utils.colorBase import ColorBase
from utils.objectBase import ObjectBase

args = sys.argv

def main():
    proceed = False

    while not proceed:
        selection = Selection()
        colorBase = ColorBase('test')
        objectBase = ObjectBase('test')
        target, object, base = selection.select()

        if base == 'Color':
            color, inverse = selection.select_color()
            if object == 'Image':
                colorBase.image_process(target, color, inverse)
                proceed = True
            elif object == 'Movie':
                colorBase.movie_process(target, color, inverse)
                proceed = True
        elif base == 'Object':
            object, inverse = selection.selected_object()
            if object == 'Image':
                objectBase.image_process(target, object, inverse)
                proceed = True
            elif object == 'Movie':
                objectBase.movie_process(target, object, inverse)
                proceed = True
        else:
            print('An error has occured!')

if __name__ == "__main__":
    main()