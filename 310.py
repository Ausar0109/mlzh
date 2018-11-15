
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
    # 点击两次弹出宝箱

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
    # 搜寻物品确认按钮

    # 左窗格110 右窗格 370
    click3(rand_choose((keyxy[0] + 110, keyxy[1] + 270), 160, 30))
    # 用来补充弹出换狗粮页面的操作
    click3(rand_choose((keyxy[0] + 176 + 50, keyxy[1] + 440), 30, 30))
    pig.moveTo(1800, 500, duration=1.5)

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

            click3(rand_choose((keyxy[0] + 110, keyxy[1] + 270), 160, 30))
            click3(rand_choose((keyxy[0] + 266, keyxy[1] + 449), 5, 5))
            pig.moveTo(1800, 500, duration=1.5)

    # 换狗粮模块
    if huangou:
        if isinstance(pig.locateCenterOnScreen(jdpath + 'dwpic/yiman.png'), tuple):
            click3(rand_choose((keyxy[0] + 350, keyxy[1] + 305), 90, 30))
            for i in range(huangou):
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

            transfer()

            click3(rand_choose((keyxy[0] + 610, keyxy[1] + 350), 90, 40))
            pig.moveTo(1800, 500, duration=3)

    print('本次运行时间:%s' % (datetime.now() - ts).seconds)
    time.sleep(5)
    transfer()

if __name__ == '__main__':
    keyxy = (0, 0)
    print(keyxy)

    while True:
        mainfunc(things='right', huangou=False, maitili=False, sikao=0.01)
