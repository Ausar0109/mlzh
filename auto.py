import pyautogui as pig
import pyautogui
from random import randint, choice
import time
from datetime import datetime

pyautogui.PAUSE = 0.8
jdpath = 'C:/Users/Administrator/Desktop/mlzh/'


def click3(xy):
    pig.moveTo(xy, tween=pig.easeInQuad, duration=0.15)
    pig.click(pause=0.101)


def rand_choose(atuple, weight, hight):
    return (atuple[0] + randint(0, weight), atuple[1] + randint(0, hight))

keyxy = input('请放置keyxy')
if keyxy == 'Y':
    keyxy = pig.position()
else:
    keyxy = (5, 5)
print("程序运行中...")


def mainfunc(things='left'):
    ts = datetime.now()
    while True:
        t1 = pig.locateCenterOnScreen(jdpath + 'dwpic/shengli.png')
        time.sleep(0.2)
        if isinstance(t1, tuple):
            break

    click3(rand_choose((keyxy[0] + 130, keyxy[1] + 100), 500, 270))
    click3(rand_choose((keyxy[0] + 130, keyxy[1] + 100), 500, 280))
    time.sleep(randint(5, 8) / 10)
    # 弹出宝箱

    if things == 'left':
        click3(rand_choose((keyxy[0] + 280, keyxy[1] + 390), 75, 35))
        time.sleep(randint(2, 3) / 10)
        click3(rand_choose((keyxy[0] + 280, keyxy[1] + 290), 30, 20))
    else:
        click3(rand_choose((keyxy[0] + 410, keyxy[1] + 345), 80, 35))
        time.sleep(randint(2, 3) / 10)

    click3(rand_choose((keyxy[0] + 400, keyxy[1] + 375), 30, 15))
    time.sleep(randint(1, 3) / 10)
    click3(rand_choose((keyxy[0] + 400, keyxy[1] + 420), 30, 8))
    time.sleep(randint(1, 4) / 10)

    # 左窗格110 右窗格 370
    click3(rand_choose((keyxy[0] + 110, keyxy[1] + 250), 160, 30))
    time.sleep(randint(2, 3) / 10)

    print('本次运行时间:%s' % (datetime.now() - ts).seconds)

if __name__ == '__main__':
    while True:
        mainfunc(things='left')
