import sys

from utils.process import Process
from utils.guiApplication import GuiApplication

args = sys.argv

def main():
    if len(sys.argv) <= 1:
        print('You need argument!')
        args.append('help')
    if args[1] == 'cui':
        proceed = False
        process = Process(proceed)

        while not proceed:
            proceed = process.run()

    elif args[1] == 'gui':
        apps = GuiApplication()
        apps = apps.apps()

    elif args[1] == 'help':
        print('python main.py cui  ---> CUI base apps')
        print('python main.py      ---> CUI base apps')
        print('python main.py gui  ---> GUI base apps')
        print('python main.py help ---> Help manu')

    else:
        print('Error is occured. Try again.')

if __name__ == "__main__":
    main()