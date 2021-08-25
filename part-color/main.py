import sys
from selection import selection as sl
from color import colorBase as cb

args = sys.argv

def main():
    selection = sl.Selection()
    colorBase = cb.ColorBase('test')
    target, object = selection.select()
    color, inverse = selection.select_color()

    if object == 'Image':
        colorBase.image_process(target, color, inverse)
    elif object == 'Movie':
        colorBase.movie_process(target, color, inverse)
    else:
        pass

if __name__ == "__main__":
    main()