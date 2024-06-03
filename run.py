import multiprocessing
import subprocess


def startJarvis():
    #code for process 1 
    print("process 1 is running")
    from main import start
    start()


def listenHotword():
    #code for process 2 
    print("process 2 is running")
    from engine.features import hotword
    hotword()


    # Start both processes
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        subprocess.call([r'device.bat'])

        p2.start()
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")
