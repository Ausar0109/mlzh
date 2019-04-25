from mlzhlc import *
import time


def get_out():
    for i in range(randint(4, 6)):
        pag.press('esc', pause=0.5)
    find_pic_andclick('不结束游戏')


def refresh_screen():
    while True:
        if find_pic_inscreen('战斗图标'):
            break
        else:
            click_in_safe()


def maitili():
    if find_pic_inscreen('礼物箱图标'):
        find_pic_andclick('礼物箱图标')
        find_pic_andclick('收取礼物箱闪电')
        find_pic_andclick('关闭礼物箱')


def get_in():
    find_pic_andclick('战斗图标', pause=2)
    countnum = 0
    while True:
        if find_pic_inscreen('卡伊洛斯地下城'):
            break
        else:
            pag.press('esc')
            find_pic_andclick('关闭限时商品')
            find_pic_andclick('关闭限时道具')
            find_pic_andclick('关闭限时道具确定')
            countnum += 1

        if countnum > 10:
            get_out()
            break


def choose_reward():
    if find_pic_inscreen('获得符石道具'):
        save_screen()
        if find_pic_inscreen('攻击速度'):
            find_pic_andclick('获得符石道具')
        elif find_pic_inscreen('稀有符文'):
            find_pic_andclick('获得符石道具', (-115, 0))
            find_pic_andclick('确认卖出符文')
        else:
            find_pic_andclick('获得符石道具')
    else:
        find_pic_andclick('战斗胜利红水',
                          randint(130, 165), pause=1)
        find_pic_andclick('确认其它道具', pause=1)
        find_pic_andclick('确认彩虹怪', pause=1)
        find_pic_andclick('确认刻印石', pause=1)


def dowith_battle(nextaction='again'):
    def next_action():
        if nextaction == 'again':
            find_pic_andclick('世界地图', (-318, -100))
            find_pic_andclick('开始战斗')
        elif nextaction == 'huicheng':
            find_pic_andclick('回城')

    if find_pic_inscreen('龙十一速'):
        find_pic_andclick('龙十一速', (-450, 2))

    if find_pic_inscreen('复活图标'):
        find_pic_andclick('复活图标', (200, 5))
        find_pic_andclick('战斗胜利闪电')
        find_pic_andclick('战斗胜利红水')
        next_action()

    if find_pic_inscreen('战斗胜利闪电'):
        find_pic_andclick('战斗胜利闪电')
        find_pic_andclick('战斗胜利红水')

        choose_reward()
        next_action()


def dixiacheng_loop():
    refresh_screen()
    get_in()

    while True:
        find_pic_andclick('卡伊洛斯地下城')
        find_pic_andclick('龙之地下城')
        find_pic_andclick('龙之地下城', (370, 115))

        if find_pic_inscreen('礼物箱图标'):
            # maitili()
            pass
        if find_pic_inscreen('商店图标'):
            break
        if find_pic_inscreen('开始战斗'):
            break

    find_pic_andclick('开始战斗')

    countnum = 0
    while True:
        if find_pic_inscreen('商店图标'):
            break

        dowith_battle('huicheng')
        find_pic_andclick('重新发送')

        if find_pic_inscreen('战斗图标'):
            break

        countnum += 1
        if countnum > 25:
            pag.press('esc')
        time.sleep(randint(10, 30))

    get_out()


def jingjichang_loop():
    refresh_screen()
    get_in()

    find_pic_andclick('竞技场图标')
    find_pic_andclick('普通竞技场')

    if find_pic_inscreen('竞技场挑战'):  # 挑战图标完好，说明没有挑战者，进入 竞技场对战
        find_pic_andclick('竞技场对战')
        find_pic_andclick('竞技场刷新', pause=3)
        find_pic_andclick('竞技场翅膀')
        find_pic_andclick('开始战斗')

    else:  # 说明有挑战者，进入 竞技场挑战
        find_pic_andclick('竞技场对战', (1, 75))

        for i in [40, 95, 140, 190, 250]:
            find_pic_andclick('挑战者翅膀', (195, i))
            find_pic_andclick('挑战者未备')
            if find_pic_inscreen('开始战斗'):
                find_pic_andclick('开始战斗')
                break
        pag.scroll(clicks=-100)
        pag.scroll(clicks=-100)
        pag.scroll(clicks=-100)
        for i in [40, 95, 140, 190, 250]:
            find_pic_andclick('挑战者翅膀', (195, i))
            find_pic_andclick('挑战者未备')
            if find_pic_inscreen('开始战斗'):
                find_pic_andclick('开始战斗')
                break

    countnum = 0
    while True:
        if find_pic_inscreen('商店图标'):
            break
        time.sleep(randint(1, 10))
        click_in_safe()

        find_pic_andclick('一速', (-450, 2))
        find_pic_andclick('二速', (-450, 2))
        find_pic_andclick('三速', (-450, 2))
        find_pic_andclick('四速', (-450, 2))
        find_pic_andclick('战斗胜利闪电')
        find_pic_andclick('竞技场名誉')
        find_pic_andclick('关闭竞技场')
        find_pic_andclick('竞技场返回')

        if find_pic_inscreen('战斗图标'):
            break

        click_in_safe()

        countnum += 1
        if countnum > 25:
            pag.press('esc')

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
                    find_pic_andclick('商店购买')
                    find_pic_andclick('商店购买2')
                    find_pic_andclick('商店购买3')
                    find_pic_andclick('购买确认')

    for i in range(4):
        find_target_in_fourblock(
            ['两星魔灵', '两星魔灵2', '神秘召唤书', '传说召唤书', '商店刻印石', '光明黑暗召唤书', '二星风赛拉德曼', '二星风仙女'])
        find_pic_andclick('魔法商店里面', (0, 100))
        pag.scroll(clicks=-1)
        pag.scroll(clicks=-1)

    for i in range(randint(3, 5)):
        pag.press('esc', pause=0.5)
    find_pic_andclick('不结束游戏')


if __name__ == '__main__':
    while True:
        shangdian_loop()
        time.sleep(randint(10, 30))
        dixiacheng_loop()
        time.sleep(randint(10, 30))
        dixiacheng_loop()
        time.sleep(randint(10, 30))
        jingjichang_loop()
        time.sleep(randint(10, 30))

        refresh_screen()
        time.sleep(randint(30, 60))
