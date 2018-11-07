import pyautogui as pig
from random import randint, choice
import time
from datetime import datetime

pig.PAUSE = 1
pig.FAILSAFE = True
jdpath = 'C:/Users/cheng.lu/Desktop/mlzh/'


def click3(xy):
    pig.moveTo(xy, tween=pig.easeInQuad, duration=0.66)
    pig.click(pause=0.22)


def rand_choose(atuple, weight, hight):
    return (atuple[0] + randint(0, weight), atuple[1] + randint(0, hight))

keyxy = (0, 0)
print("程序开始运行...")


def mainfunc(things='left', huangou=True, maitili=False):
    ts = datetime.now()
    while True:
        t1 = pig.locateCenterOnScreen(jdpath + 'dwpic/shengli.png')
        time.sleep(1.5)
        if isinstance(t1, tuple):
            break

    click3(rand_choose((keyxy[0] + 130, keyxy[1] + 100), 500, 270))
    click3(rand_choose((keyxy[0] + 130, keyxy[1] + 100), 500, 280))
    time.sleep(randint(5, 8) / 10)
    # 弹出宝箱

    if things == 'left':
        click3(rand_choose((keyxy[0] + 280, keyxy[1] + 400), 75, 35))
        time.sleep(randint(2, 3) / 10)
        click3(rand_choose((keyxy[0] + 280, keyxy[1] + 290), 30, 20))
    else:
        click3(rand_choose((keyxy[0] + 410, keyxy[1] + 345), 80, 35))
        time.sleep(randint(2, 3) / 10)

    click3(rand_choose((keyxy[0] + 400, keyxy[1] + 375), 30, 15))
    time.sleep(randint(1, 3) / 10)
    click3(rand_choose((keyxy[0] + 350, keyxy[1] + 420), 30, 8))
    time.sleep(randint(1, 4) / 10)

    # 左窗格110 右窗格 370
    click3(rand_choose((keyxy[0] + 110, keyxy[1] + 270), 160, 30))
    pig.moveTo(1800, 500, duration=3)
    time.sleep(randint(2, 3) / 10)

    # 买体力模块
    if maitili:
        if isinstance(pig.locateCenterOnScreen(jdpath + 'dwpic/shangdian.png'), tuple):
            click3(rand_choose((keyxy[0] + 265, keyxy[1] + 320), 90, 30))
            time.sleep(2)

            click3(rand_choose((keyxy[0] + 260, keyxy[1] + 225), 120, 100))
            time.sleep(2)
            click3(rand_choose((keyxy[0] + 280, keyxy[1] + 310), 80, 35))
            time.sleep(2)
            click3(rand_choose((keyxy[0] + 355, keyxy[1] + 310), 60, 30))
            time.sleep(2)
            click3(rand_choose((keyxy[0] + 360, keyxy[1] + 430), 60, 30))
            time.sleep(2)

            click3(rand_choose((keyxy[0] + 110, keyxy[1] + 250), 160, 30))
            click3(rand_choose((keyxy[0] + 266, keyxy[1] + 449), 5, 5))
            pig.moveTo(1800, 500, duration=3)

    # 换狗粮模块
    if huangou:
        if isinstance(pig.locateCenterOnScreen(jdpath + 'dwpic/yiman.png'), tuple):
            click3(rand_choose((keyxy[0] + 350, keyxy[1] + 305), 90, 30))
            for i in range(15):
                pig.moveTo((keyxy[0] + 545, keyxy[1] + 340 + randint(0, 5)))
                pig.dragTo(keyxy[0] + 15, keyxy[1] + 340 +
                           randint(0, 5), duration=randint(5, 15) / 12, button='left')
            time.sleep(5)
            click3(rand_choose((keyxy[0] + 90, keyxy[1] + 180), 50, 50))
            click3(rand_choose((keyxy[0] + 265, keyxy[1] + 180), 50, 50))
            click3(rand_choose((keyxy[0] + 180, keyxy[1] + 225), 50, 50))

            click3(rand_choose((keyxy[0] + 325, keyxy[1] + 335), 40, 38))
            click3(rand_choose((keyxy[0] + 400, keyxy[1] + 335), 40, 38))
            click3(rand_choose((keyxy[0] + 475, keyxy[1] + 335), 40, 38))

            click3(rand_choose((keyxy[0] + 610, keyxy[1] + 350), 90, 40))
            pig.moveTo(1800, 500, duration=3)

    print('本次运行时间:%s' % (datetime.now() - ts).seconds)

if __name__ == '__main__':
    keyxy = (0, 0)
    print(keyxy)
    while True:
        mainfunc(things='left', huangou=True, maitili=False)
