from mlzhlc import *
import time


def dixiacheng_action_after_findpic(shangdian=False):
    #find_pic_andclick('复活图标', (200,5)) #

    #find_pic_andclick('战斗胜利闪电') #
    find_pic_andclick('战斗胜利红水', (-177, randint(120, 150)))
    find_pic_andclick('战斗胜利红水', (-177, randint(150, 180)))

    # find_pic_andclick('获得符石道具')
    # find_pic_andclick('确认其它道具')
    # find_pic_andclick('确认彩虹怪')
    #find_pic_andclick('确认刻印石', pause=0.5)

    find_pic_andclick('世界地图', (-318, -100), pause=0.5)
    # find_pic_andclick('开始战斗')

    if shangdian:
        if find_pic_inscreen('商店图标'):
            find_pic_andclick('礼物箱图标')
            find_pic_andclick('收取礼物箱闪电')
            find_pic_andclick('关闭礼物箱')
            find_pic_andclick('世界地图', (-318, -100))

if __name__ == '__main__':
    while True:
        click_in_safe()
        click_in_safe()
        dixiacheng_action_after_findpic(0)
