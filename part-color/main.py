import sys
from select import select as sl
from color import colorBase as cb

args = sys.argv

def main():
    select = sl.Select()
    colorBase = cb.ColorBase('test')
    target, object = select.select()
    color, inverse = select.select_color()

    if object == 'Image':
        colorBase.image_process(target, color, inverse)
    elif object == 'Movie':
        colorBase.movie_process(target, color, inverse)
    else:
        pass

if __name__ == "__main__":
    main()