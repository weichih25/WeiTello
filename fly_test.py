from time import sleep
from tello import Tello
import threading

def _telloA():
    tello = Tello('192.168.50.201',8889)
    tello.send_command('command')
    sleep(1)
    tello.send_command('speed 80')
    sleep(1)
    tello.send_command('battery?')
    sleep(1)
    tello.send_command('takeoff')
    sleep(2)
    tello.send_command('up 150')
    sleep(1)
    for i in range(2):
        tello.send_command('forward 200')
        sleep(1)
        tello.send_command('left 200')
        sleep(1)
        tello.send_command('back 200')
        sleep(1)
        tello.send_command('right 200')

    sleep(1)
    tello.send_command('land')
'''
def _telloB():
    tello = Tello('192.168.50.201',9000)
    tello.send_command('command')
    sleep(0.1)
    tello.send_command('speed 80')
    sleep(0.1)
    tello.send_command('battery?')
    sleep(0.1)
    tello.send_command('takeoff')
    sleep(2)
    tello.send_command('up 50')
    sleep(1)
    tello.send_command('forward 300')
    sleep(1)
    tello.send_command('left 250')
    sleep(1)
    tello.send_command('right 250')
    sleep(1)
    tello.send_command('back 300')
    sleep(1)
    tello.send_command('land')
'''

def main():
    print('start :)')
    thread_telloA = threading.Thread(target=_telloA, name='T1')
    thread_telloA.start()
    '''
    sleep(3)
    thread_telloB = threading.Thread(target=_telloB, name='T2')
    thread_telloB.start()
    '''
  

if __name__ == '__main__':
    main()
