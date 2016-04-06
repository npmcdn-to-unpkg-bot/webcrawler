from multiprocessing import Process
import time


def process_A():
    print('process 1 running')
    time.sleep(5)
    print('process 1 running again')


def process_B():
    print('process 2 running')
    time.sleep(2)
    print('process 2 running again')

'''
start后p1,p2会不断切换运行，join之后依然会不断切换运行，
只是要等join的调用者在切换调用的过程中运行完毕之后才会向下执行
既：在join前start的函数都会不断切换执行，若有函数调用join，
则需在切换不断调用的过程中等待该函数执行完成后才开始执行join以下的代码
'''
if __name__ == '__main__':
    p1 = Process(target=process_A)
    p2 = Process(target=process_B)
    p1.start()
    p2.start()
    p1.join()
    # p2.join()
    # time.sleep(10)
    print('Back to main process')