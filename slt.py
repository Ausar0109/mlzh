import pyautogui as pig
from random import randint, choice
import time
from datetime import datetime

pig.PAUSE = 0.5
pig.FAILSAFE = True
jdpath = 'C:/Users/cheng.lu/Desktop/mlzh/'


def click3(xy):
    pig.moveTo(xy, tween=pig.easeInQuad, duration=0.66)
    pig.click(pause=0.22)


def rand_choose(atuple, weight, hight):
    return (atuple[0] + randint(0, weight), atuple[1] + randint(0, hight))


def transfer():
    pig.moveTo(rand_choose((keyxy[0] + 50, keyxy[1] + 50), 600, 300))
    pig.hotkey('ctrl', 'alt', 'a')

    click3(rand_choose((keyxy[0] + 50, keyxy[1] + 50), 600, 30))
    click3(rand_choose((keyxy[0] + 765, keyxy[1] + 529), 2, 2))

    click3(rand_choose((keyxy[0] + 1282, keyxy[1] + 502), 2, 2))
    time.sleep(1)  # 变化
    pig.hotkey('ctrl', 'v')

keyxy = (0, 0)
print("程序开始运行...")


def mainfunc(things='left', huangou=True, maitili=False, sikao=True):
    ts = datetime.now()
    jiancecishu = 0
    while True:
        t1 = pig.locateCenterOnScreen(jdpath + 'dwpic/shengli.png')
        time.sleep(1.5)
        if isinstance(t1, tuple):
            break

        t2 = pig.locateCenterOnScreen(jdpath + 'dwpic/siwang.png')
        time.sleep(1.5)
        if isinstance(t2, tuple):
            transfer()
            click3(rand_choose((keyxy[0] + 450, keyxy[1] + 325), 150, 40))
            click3(rand_choose((keyxy[0] + 130, keyxy[1] + 100), 500, 270))
            click3(rand_choose((keyxy[0] + 110, keyxy[1] + 270), 160, 30))
            click3(rand_choose((keyxy[0] + 610, keyxy[1] + 350), 90, 40))
            pig.moveTo(1800, 500, duration=1.5)
            break

        jiancecishu += 1
        if jiancecishu % 200 == 0:
            transfer()

    click3(rand_choose((keyxy[0] + 130, keyxy[1] + 100), 500, 270))
    click3(rand_choose((keyxy[0] + 130, keyxy[1] + 100), 500, 280))
    # 弹出宝箱

    if sikao:
        pig.moveTo(rand_choose((keyxy[0] + 50, keyxy[1] + 50), 600, 300))
        sikaoshijian = 230 * sikao * randint(65, 135) / 100
        sikaoshijian = sikaoshijian // 1
        print('本次思考时间-----------【 %s 】' % sikaoshijian)

        transfer()
        time.sleep(sikaoshijian)

    if things == 'left':
        click3(rand_choose((keyxy[0] + 280, keyxy[1] + 400), 75, 35))
        time.sleep(randint(2, 3) / 10)
    elif things == 'left2':
        click3(rand_choose((keyxy[0] + 280, keyxy[1] + 400), 75, 35))
        time.sleep(randint(2, 3) / 10)
        pig.moveTo(keyxy[0] + 280, keyxy[1] + 305)
        click3(rand_choose((keyxy[0] + 275, keyxy[1] + 310), 30, 18))
    else:
        click3(rand_choose((keyxy[0] + 420, keyxy[1] + 405), 70, 30))
        time.sleep(randint(2, 3) / 10)

    click3(rand_choose((keyxy[0] + 379, keyxy[1] + 380), 20, 20))
    click3(rand_choose((keyxy[0] + 379, keyxy[1] + 420), 20, 8))

    # 左窗格110 右窗格 370
    click3(rand_choose((keyxy[0] + 110, keyxy[1] + 270), 160, 30))
    #click3(rand_choose((keyxy[0] + 176 + 50, keyxy[1] + 440), 30, 30))
    click3(rand_choose((keyxy[0] + 610, keyxy[1] + 350), 90, 40))
    pig.moveTo(1800, 500, duration=1.5)

    print('本次运行时间:%s' % (datetime.now() - ts).seconds)
    time.sleep(5)
    transfer()

if __name__ == '__main__':
    keyxy = (0, 0)
    print(keyxy)

    while True:
        mainfunc(things='right', sikao=0.01)
