import sys
from select_by import selectByUser as su
from color import colorBase as cb

args = sys.argv

def main():
    selectByUser = su.SelectByUser()
    colorBase = cb.ColorBase('test')
    target, object = selectByUser.select()
    color, inverse = selectByUser.select_color()

    if object == 'Image':
        colorBase.image_process(target, color, inverse)
    elif object == 'Movie':
        colorBase.movie_process(target, color, inverse)
    else:
        pass

if __name__ == "__main__":
    main()