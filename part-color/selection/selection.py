import os

class Selection():
    def __init__(self):
        self.target = ''
        self.object = ''
        self.base = ''
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

        image_selecting = True
        list_datas = os.listdir(DIR)
        print(list_datas)
        while image_selecting:
            self.target = input('Which do you want to process? >> ')
            self.target = str(self.target)
            image_selecting != os.path.exists('./DIR/' + self.target)

        while True:
            self.base = input('[C]olor base or [O]bject base? >> ')
            if self.base == 'C' or self.base == 'Color':
                self.object = 'Color'
                break
            elif self.base == 'O' or self.base == 'Object':
                self.base = 'Object'
                break
            else:
                pass

        return self.target, self.object, self.base

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