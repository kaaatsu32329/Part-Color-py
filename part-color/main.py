from utils.process import Process

def main():
    proceed = False
    process = Process(proceed)

    while not proceed:
        proceed = process.run()

if __name__ == "__main__":
    main()