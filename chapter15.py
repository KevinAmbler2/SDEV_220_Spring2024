import multiprocessing, time, random, datetime

def outputTime():
    time.sleep(random.random())
    print("The current time is "+str(datetime.datetime.now().time()))

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=outputTime())
    process2 = multiprocessing.Process(target=outputTime())
    process3 = multiprocessing.Process(target=outputTime())
    process1.start()
    process2.start()
    process3.start()

    print('Processes completed')