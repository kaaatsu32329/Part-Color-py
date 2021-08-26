import os

class Selection():
    def __init__(self):
        self.target = ''
        self.object = ''
        self.selected = ''
        self.inverse = 0

    def select(self):
        while True:
            self.object = input('[I]mage or [M]ovie? >> ')
            if self.object == 'I' or self.object == 'Image':
                DIR = '../sample_images/'
                self.object = 'Image'
                break
            elif self.object == 'M' or self.object == 'Movie':
                DIR = '../sample_movies/'
                self.object = 'Movie'
                break
            else:
                pass
        list_datas = os.listdir(DIR)
        print(list_datas)
        self.target = input('Which do you want to process? >> ')
        self.target = str(self.target)
        return self.target, self.object

    def select_color(self):
        print('Which color will you use?')
        self.selected = input('red, green, blue, orange >> ')
        self.selected = str(self.selected)
        self.inverse = input('Inversion? [y]es/[n]o >> ')
        if self.inverse == 'y' or self.inverse == 'yes':
            self.inverse = True
        else:
            self.inverse = False
        return self.selected, self.inverse