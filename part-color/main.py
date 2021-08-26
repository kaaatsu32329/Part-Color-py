import sys
from selection import selection as sl
from color import colorBase as cb

args = sys.argv

def main():
    proceed = False

    while not proceed:
        selection = sl.Selection()
        colorBase = cb.ColorBase('test')
        target, object, base = selection.select()
        color, inverse = selection.select_color()

        if object == 'Image':
            if base == 'Color':
                colorBase.image_process(target, color, inverse)
                proceed = True
            elif base == 'Object':
                proceed = True
            else:
                pass
        elif object == 'Movie':
            if base == 'Color':
                colorBase.movie_process(target, color, inverse)
                proceed = True
            elif base == 'Object':
                proceed = True
            else:
                pass
        else:
            print('An error has occured!')

if __name__ == "__main__":
    main()