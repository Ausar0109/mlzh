import pyautogui as pig
from random import randint, choice
import time
from datetime import datetime

pig.PAUSE = 0.5
pig.FAILSAFE = True
jdpath = 'C:/Users/cheng.lu/Desktop/mlzh/'

zbx = {
    'window': [(20, 100), 600, 200],
    'zailaiyici': [(110, 235), 180, 30],
    'kaishizhandou': [(520, 300), 100, 40],
    'haoyou': [(210, 380), 20, 20],

    'fw-left': [(240, 340), 80, 30],
    'fw-sold': [(240, 260), 80, 30],
    'fw-right': [(360, 340), 80, 30],

    'wupin1': [(300, 320), 30, 30],
    'wupin2': [(300, 360), 25, 15],

    'bufuhuo': [(380, 280), 100, 30],

    'jietu-queding': [(645, 455), 2, 2],
    'QQ-blank': [(1131, 707), 2, 2],
    'outwindow': [(1200, 600), 2, 2],

    'shangdian1': [(210, 210), 80, 80],
    'shangdian2': [(230, 265), 70, 25],
    'shangdian3': [(300, 260), 80, 30],
    'shangdian4': [(300, 360), 70, 20],

    'w1': [(75, 155), 35, 35],
    'w2': [(225, 155), 35, 35],
    'w3': [(150, 200), 35, 35],

    'move-left': [(30, 290), 5, 30],
    'move-right': [(465, 295), 5, 30],

    'm1': [(280, 290), 30, 30],
    'm2': [(340, 290), 30, 30],
    'm3': [(400, 290), 30, 30]}


def rand_choose(zuobiao_pack):
    '''输入方框参数 列表[(0,0),100,100]
       返回该方框内的随机坐标'''
    atuple = zuobiao_pack[0]
    weight = zuobiao_pack[1]
    hight = zuobiao_pack[2]
    return (atuple[0] + randint(0, weight), atuple[1] + randint(0, hight))


def click3(zuobiao_pack):
    '''输入方框参数 列表[(0,0),100,100]
       返回该方框内的随机坐标
       并触发点击行为'''
    xy = rand_choose(zuobiao_pack)
    pig.moveTo(xy, tween=pig.easeInQuad, duration=0.8)
    pig.click(pause=0.101)
    pig.moveTo(xy, pause=0.101)


def transfer():
    # pig.moveTo(rand_choose(zbx['window']))
    pig.hotkey('ctrl', 'alt', 'a')

    click3(zbx['window'])
    click3(zbx['jietu-queding'])

    click3(zbx['QQ-blank'])
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
            click3(zbx['bufuhuo'])  # 不复活
            click3(zbx['window'])  # 点击window确认
            click3(zbx['zailaiyici'])  # 点击再来一次 进入复活准备页面
            click3(zbx['kaishizhandou'])  # 开始战斗
            pig.moveTo(rand_choose(zbx['outwindow']))
            break

        jiancecishu += 1
        if jiancecishu % 200 == 0:
            transfer()

    click3(zbx['window'])
    click3(zbx['window'])
    # 点击两次弹出宝箱

    if sikao:
        pig.moveTo(rand_choose(zbx['outwindow']), duration=2)
        sikaoshijian = 230 * sikao * randint(65, 135) / 100
        sikaoshijian = sikaoshijian // 1
        print('本次思考时间-----------【 %s 】' % sikaoshijian)

        transfer()
        time.sleep(sikaoshijian)

    if things == 'left':
        click3(zbx['fw-left'])
    elif things == 'left2':
        click3(zbx['fw-left'])
        pig.moveTo(rand_choose(zbx['fw-sold']), pause=1.5)  # 给缓冲时间
        click3(zbx['fw-sold'])
    else:
        click3(zbx['fw-right'])

    click3(zbx['wupin1'])
    click3(zbx['wupin2'])
    # 搜寻物品确认按钮

    # 左窗格110 右窗格 370
    click3(zbx['zailaiyici'])
    # 用来补充弹出换狗粮页面的操作
    click3([(25, 365), 20, 20])
    click3(zbx['kaishizhandou'])
    pig.moveTo(rand_choose(zbx['outwindow']), duration=1.5)

    print('本次运行时间:%s' % (datetime.now() - ts).seconds)
    time.sleep(6)
    transfer()

if __name__ == '__main__':
    keyxy = (0, 0)
    print(keyxy)

    while True:
        mainfunc(things='right', huangou=False, maitili=False, sikao=False)
