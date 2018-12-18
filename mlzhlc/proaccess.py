from .action import ppaste, rand_choose, click3
from .action import zbx
from .action import find_pic, find_pic_click, tfind_pic_click, transfer
from .action import ccenter

from .action import pig
import time
from datetime import datetime, timedelta

#minute_70 = datetime(2018, 1, 1, 1, 0) - datetime(2018, 1, 1, 0, 0)


def login(yidi=True):
    if yidi:
        find_pic_click('yididenglu')

    ccenter('开始检测登陆界面....')
    while True:
        if isinstance(find_pic('denglu'), tuple):
            break
        time.sleep(2)
    click3(zbx['mima'])
    time.sleep(2)

    ppaste('apple7342001')
    find_pic_click('denglu', timesleep=2)
    find_pic_click('denglu', timesleep=2)
    time.sleep(60)

    for i in range(4):
        find_pic_click('login_ad', timesleep=2)
    for i in range(4):
        find_pic_click('yanchi', timesleep=0)

    click3(zbx['touchtostart'])
    time.sleep(10)

    if not isinstance(find_pic('liwu-guanbi'), tuple):
        click3(zbx['goumaidaoju-guanbi'])
        click3(zbx['goumaidaoju-guanbi2'])
    tfind_pic_click('liwu-guanbi')


def ShangDian_SouSuo():
    ccenter('商店开始检测...')
    while True:
        if isinstance(find_pic('zhandou', timesleep=5), tuple):
            break
    click3(zbx['shangdian'])
    click3(zbx['shangdian-goumai'])

    def jiance():
        if isinstance(find_pic('shangdian-shenmi', 5), tuple):
            transfer()
            find_pic_click('shangdian-goumai', 2)
            find_pic_click('shangdian-queding', 2)
        # if isinstance(find_pic('shangdian-weizhi', 0), tuple):
        #    transfer()
        #    find_pic_click('shangdian-goumai', 2)
        #    find_pic_click('shangdian-queding', 2)
        if isinstance(find_pic('shangdian-keyin', 0), tuple):
            transfer()
            find_pic_click('shangdian-goumai', 2)
            find_pic_click('shangdian-queding', 2)
        if isinstance(find_pic('shangdian-guangming', 0), tuple):
            transfer()
            find_pic_click('shangdian-goumai', 2)
            find_pic_click('shangdian-queding', 2)
        if isinstance(find_pic('shangdian-liangxing', 0), tuple):
            transfer()
            find_pic_click('shangdian-gouliang', 2)
            find_pic_click('shangdian-queding', 2)

    click3([(400, 135), 200, 60])
    jiance()
    click3([(400, 200), 200, 60])
    jiance()
    click3([(400, 265), 200, 60])
    jiance()

    for i in range(6):
        pig.moveTo(rand_choose([(400, 295), 200, 5]),
                   tween=pig.easeInQuad, pause=0.1)
        pig.dragTo(rand_choose([(400, 180), 200, 5]),
                   tween=pig.easeInQuad, pause=0.2, duration=1)
        click3([(400, 145), 200, 40])
        jiance()
        click3([(400, 210), 200, 40])
        jiance()
        click3([(400, 275), 200, 40])
        jiance()

    click3([(400, 350), 200, 10])
    jiance()

    click3(zbx['shangdian-guanbi'])


def get_in(doorname):
    tfind_pic_click('zhandou')
    if not isinstance(find_pic('dixiacheng', 4), tuple):
        click3(zbx['goumaidaoju-guanbi'])
        click3(zbx['goumaidaoju-guanbi2'])
        find_pic_click('goumaidaoju-guanbiquding')
    tfind_pic_click('dixiacheng')

    if doorname == 'juren':
        while True:
            click3(zbx['dishiceng'])
            xy = find_pic('juren10')
            if isinstance(xy, tuple):
                click3(zbx['kaishizhandou'])
                time.sleep(10)
                if isinstance(find_pic('fengge'), tuple):
                    click3(zbx['autobutton'])

                break
            else:
                click3(zbx['jieshuzhandou'])
                time.sleep(2)
                click3(zbx['julong'])
                click3(zbx['juren'])
    elif doorname == 'julong':
        click3(zbx['julong'])
        while True:
            click3(zbx['dishiceng'])
            xy = find_pic('julong10')
            if isinstance(xy, tuple):
                click3(zbx['kaishizhandou'])
                time.sleep(20)
                if isinstance(find_pic('huoxi'), tuple):
                    click3(zbx['autobutton'])

                break
            else:
                click3(zbx['jieshuzhandou'])
                time.sleep(2)
                click3(zbx['juren'])
                click3(zbx['julong'])


def loopmlzh(loopnumber=3):

    for i in range(loopnumber):
        ccenter('开始检测...')
        statess = True
        while True:
            t1 = find_pic('shengli')
            time.sleep(15)
            if isinstance(t1, tuple):
                break
            find_pic_click('duanwang', timesleep=0)

            t2 = find_pic('siwang')
            if isinstance(t2, tuple):
                transfer()
                statess = False
                break

        if statess:
            click3(zbx['window'], zbx['window'])
            time.sleep(2)
            transfer()
            click3(zbx['fw-right'])
            click3(zbx['wupin1'])
            click3(zbx['wupin2'])

            find_pic_click('shengdan')

            if i == loopnumber - 1:
                click3(zbx['huicheng'])
                break
            else:
                click3(zbx['zailaiyici'])
                if isinstance(find_pic('shangdian'), tuple):
                    transfer()
                    click3(zbx['no-energy'])
                    click3(zbx['huicheng'])
                    break
        else:
            click3(zbx['bufuhuo'], zbx['window'])
            if i == loopnumber - 1:
                click3(zbx['huicheng'])
            else:
                click3(zbx['zailaiyici'])
                if isinstance(find_pic('shangdian'), tuple):
                    transfer()
                    click3(zbx['no-energy'])
                    click3(zbx['huicheng'])
                    break
                click3(zbx['kaishizhandou'])

    if not isinstance(find_pic('zhandou'), tuple):
        click3(zbx['goumaidaoju-guanbi'])
        click3(zbx['goumaidaoju-guanbi2'])
