from utils.process import Process

def cui_applciation():
    proceed = False
    process = Process(proceed)

    while not proceed:
        proceed = process.run()