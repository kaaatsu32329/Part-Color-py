import os

class SelectByUser():
    def __init__(self):
        self.target = ''
        self.object = ''
        self.selected = ''
        self.inverse = 0

    def select(self):
        while True:
            object = input('[I]mage or [M]ovie? >> ')
            if object == 'I' or object == 'Image':
                dir = '../sample_images/'
                object = 'Image'
                break
            elif object == 'M' or object == 'Movie':
                dir = '../sample_movies/'
                object = 'Movie'
                break
            else:
                pass
        list_datas = os.listdir(dir)
        print(list_datas)
        target = input('Which do you want to process? >> ')
        target = str(target)
        return target, object

    def select_color(self):
        print('Which color will you use?')
        selected = input('red, green, blue, orange >> ')
        selected = str(selected)
        inverse = input('Inversion? [y]es/[n]o >> ')
        if inverse == 'y' or inverse == 'yes':
            inverse = True
        else:
            inverse = False
        return selected, inverse