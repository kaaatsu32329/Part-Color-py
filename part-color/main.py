import sys
from utils.selection import selection as sl
from utils.colorBase import colorBase as cb
from utils.objectBase import objectBase as ob

args = sys.argv

def main():
    proceed = False

    while not proceed:
        selection = sl.Selection()
        colorBase = cb.ColorBase('test')
        objectBase = ob.ObjectBase('test')
        target, object, base = selection.select()

        if base == 'Color':
            color, inverse = selection.select_color()
            if object == 'Image':
                colorBase.image_process(target, color, inverse)
                proceed = True
            elif object == 'Movie':
                colorBase.movie_process(target, color, inverse)
                proceed = True
            else:
                pass
        elif base == 'Object':
            object, inverse = selection.selected_object()
            if object == 'Image':
                objectBase.image_process(target, object, inverse)
                proceed = True
            elif object == 'Movie':
                objectBase.movie_process(target, object, inverse)
                proceed = True
            else:
                pass
        else:
            print('An error has occured!')

if __name__ == "__main__":
    main()