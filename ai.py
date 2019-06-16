from mlzhlc import *
import time
from random import choice
from datetime import datetime

randomlist = [1] * 155 + [987] * 3
yijielist = [1] * 50 + [2] * 20 + [3, 4, 5] * 5
print(randomlist)


def get_out():
    while not find_pic_inscreen('战斗图标'):
        find_pic_andclick('不结束游戏')
        pag.press('esc', pause=0.5)
        click_in_safe()
        find_pic_andclick('关闭限时道具确定')
        find_pic_andclick('不结束游戏')


def refresh_screen():
    while not find_pic_inscreen('战斗图标'):  # Break 点位
        click_in_safe()


def maitili():
    if find_pic_inscreen('礼物箱图标'):
        find_pic_andclick('礼物箱图标')
        find_pic_andclick('收取礼物箱闪电')
        find_pic_andclick('关闭礼物箱')


def get_in():
    while True:
        if find_pic_inscreen('战斗图标'):
            find_pic_andclick('战斗图标')
        elif find_pic_inscreen('卡伊洛斯地下城'):
            break
        else:
            pag.press('esc', pause=2)
            find_pic_andclick('关闭限时道具确定')


def choose_reward():
    if find_pic_inscreen('获得符石道具'):
        find_pic_andclick('获得符石道具')
    else:
        find_pic_andclick('战斗胜利红水', (-177, 110))
        find_pic_andclick('战斗胜利红水', (-177, 140))
        find_pic_andclick('战斗胜利红水', (-177, 170))


def dowith_battle():
    if find_pic_inscreen('复活图标'):
        save_screen()
        find_pic_andclick('复活图标', (200, 5))
        find_pic_andclick('战斗胜利闪电')
        find_pic_andclick('战斗胜利红水')

    if find_pic_inscreen('战斗胜利红水'):
        save_screen()
        find_pic_andclick('战斗胜利闪电')
        find_pic_andclick('战斗胜利红水')
        choose_reward()  # 接上


def dixiacheng_loop(dornum, scroll=False):
    refresh_screen()
    get_in()

    while not find_pic_inscreen('开始战斗'):
        find_pic_andclick('卡伊洛斯地下城')

        if scroll:
            find_pic_andclick('卡伊洛斯地下城门牌', (-140, 100))
            pag.scroll(clicks=-50)
            pag.scroll(clicks=-50)

        find_pic_andclick('卡伊洛斯地下城门牌', (-140, 40 + 60 * dornum))
        find_pic_andclick('卡伊洛斯地下城门牌', (260, 285))

        if find_pic_inscreen('商店图标'):
            if choice(randomlist) == 987:
                maitili()
            else:
                break

    find_pic_andclick('开始战斗')
    save_screen()

    while True:
        if find_pic_inscreen('商店图标'):
            break

        dowith_battle()
        find_pic_andclick('南瓜', (-445, 2))
        find_pic_andclick('重新发送')

        if find_pic_inscreen('回城'):
            find_pic_andclick('回城')
            break

    get_out()


def jingjichang_loop():
    refresh_screen()
    get_in()

    while not find_pic_inscreen('竞技场对战'):
        find_pic_andclick('竞技场图标')
        find_pic_andclick('普通竞技场')

    time.sleep(5)
    if find_pic_inscreen('竞技场挑战'):  # 挑战图标完好，说明没有挑战者，进入 竞技场对战
        find_pic_andclick('竞技场对战', pause=3)
        find_pic_andclick('竞技场刷新', pause=3)
        find_pic_andclick('竞技场翅膀', pause=3)
        find_pic_andclick('开始战斗')

    else:  # 说明有挑战者，进入 竞技场挑战
        find_pic_andclick('竞技场对战', (1, 75), pause=3)

        for i in [40, 95, 140, 190, 250]:
            find_pic_andclick('挑战者翅膀', (195, i), pause=3)
            find_pic_andclick('挑战者未备', pause=3)
            if find_pic_inscreen('开始战斗'):
                find_pic_andclick('开始战斗')
                break

        pag.scroll(clicks=-100)
        pag.scroll(clicks=-100)
        pag.scroll(clicks=-100)

        for i in [40, 95, 140, 190, 250]:
            find_pic_andclick('挑战者翅膀', (195, i), pause=3)
            find_pic_andclick('挑战者未备', pause=3)
            if find_pic_inscreen('开始战斗'):
                find_pic_andclick('开始战斗')
                break

    find_pic_andclick('挑战者未备', pause=3)
    find_pic_andclick('开始战斗')
    save_screen()
    countnum = 0

    while True:
        if find_pic_inscreen('商店图标'):
            break
        time.sleep(randint(1, 10))
        click_in_safe()
        click_in_safe()

        find_pic_andclick('一速', (-442, 2))
        find_pic_andclick('二速', (-442, 2))
        find_pic_andclick('三速', (-445, 2))
        find_pic_andclick('四速', (-445, 2))

        find_pic_andclick('关闭竞技场')

        if find_pic_inscreen('竞技场返回'):
            find_pic_andclick('竞技场返回')
            break

        if find_pic_inscreen('战斗图标'):
            break
        if find_pic_inscreen('卡伊洛斯地下城'):
            break

        countnum += 1
        if countnum > 10:
            find_pic_andclick('防御之塔', (-517, 304))

    get_out()


def shangdian_loop():
    while True:
        click_in_safe()
        time.sleep(2)
        find_pic_andclick('战斗图标', (-55, -165))
        if find_pic_inscreen('商店信息图标'):
            find_pic_andclick('商店信息图标', (-70, 0))
            break

    def find_target_in_fourblock(target):
        for i in [90, 150, 210, 270]:
            find_pic_andclick('魔法商店里面', (0, i), pause=1)
            for k in target:
                if find_pic_inscreen(k):
                    save_screen(k)
                    find_pic_andclick('魔法商店里面', (-380, 235))
                    find_pic_andclick('购买确认')

    for i in range(4):
        save_screen()
        find_target_in_fourblock(
            ['神秘召唤书', '商店刻印石', '光明黑暗召唤书'] + ['两星魔灵', '两星魔灵2'])  #
        find_pic_andclick('魔法商店里面', (0, 100))
        pag.scroll(clicks=-1)
        pag.scroll(clicks=-1)

    get_out()


def yijie_loop(getnum):
    refresh_screen()
    get_in()

    while not find_pic_inscreen('开始战斗'):
        find_pic_andclick('卡伊洛斯地下城', (155, 1))
        find_pic_andclick('确认卖出符文')
        find_pic_andclick('焰火地下城')

        find_pic_andclick('异界地下城门牌', (-20 + 50 * getnum, 45))
        find_pic_andclick('进行战斗')

        if find_pic_inscreen('商店图标'):
            if choice(randomlist) == 987:
                maitili()
            else:
                break

    find_pic_andclick('开始战斗')

    while True:
        time.sleep(randint(5, 25))
        click_in_safe()

        if find_pic_inscreen('商店图标'):
            break

        if find_pic_inscreen('异界地下城结算'):
            save_screen()
            find_pic_andclick('异界地下城结算')
            find_pic_andclick('异界回城')
            break

    get_out()


def jiance_login(tim=20):
    save_screen('检测开始 %s分钟' % tim)
    ts = datetime.now()
    tmax = datetime(2000, 1, 1, 1, tim + randint(-2, 2), 0)
    tmin = datetime(2000, 1, 1, 1, 0, 0)
    tmm = tmax - tmin

    while True:
        click_in_safe(10)
        if find_pic_inscreen('登录已过期'):

            save_screen('计时60分钟')
            for i in range(60 * 60 // 30):
               click_in_safe()
               time.sleep(randint(20, 40))

            find_pic_andclick('登录已过期', (1, 82))
            find_pic_andclick('登录已过期', (1, 82))
            find_pic_andclick('密码', (0, 0), qianzhi=30, pause=5)
            ppaste('apple7342001')
            find_pic_andclick('登录按钮', qianzhi=5, pause=30)

            while not find_pic_inscreen('战斗图标'):
                pag.press('esc', pause=3)

                if find_pic_inscreen('不结束游戏'):
                    find_pic_andclick('不结束游戏')
                    click_in_safe()
            break

        if datetime.now() - ts > tmm:
            break


if __name__ == '__main__':
    get_out()
    countnum = 0
    while True:
        save_screen('循环开始')
        dixiacheng_loop(4)

        chos = randint(4, 50)
        if chos < 3:
            loca = 3 if datetime.now().weekday() in [0, 1, 2, 3, 6] else 4
            dixiacheng_loop(loca, 1)
            dixiacheng_loop(4, 1)
        elif chos <= 10:
            dixiacheng_loop(4)
        elif chos <= 15:
            dixiacheng_loop(choice([4, 4]))
        else:
            yijie_loop(choice(yijielist))

        jingjichang_loop()

        countnum += 1
        if countnum % 4 == 0:
            shangdian_loop()

        jiance_login(10)
