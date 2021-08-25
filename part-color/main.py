import sys
from color import colorBase as cb

args = sys.argv

def main():
    colorBase = cb.colorBase('test')
    target, object = colorBase.select()

    if object == 'Image':
        colorBase.image_process(target)
    elif object == 'Movie':
        colorBase.movie_process(target)
    else:
        pass

if __name__ == "__main__":
    main()