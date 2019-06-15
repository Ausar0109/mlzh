from mlzhlc import *
import time


def daigouliang():
    #find_pic_andclick('复活图标', (200, 5))

    find_pic_andclick('战斗胜利红水', (-177, 110), qianzhi=0, pause=0)
    find_pic_andclick('战斗胜利红水', (-177, 150), qianzhi=0, pause=0)
    find_pic_andclick('获得符石道具', (-115, 0), qianzhi=0, pause=0)
    find_pic_andclick('确认卖出符文', qianzhi=0, pause=0)

    find_pic_andclick('世界地图', (-318, -100), qianzhi=0, pause=0)

    # if find_pic_inscreen('商店图标'):
    #    find_pic_andclick('礼物箱图标')
    #    find_pic_andclick('收取礼物箱闪电')
    #    find_pic_andclick('关闭礼物箱')
    #    find_pic_andclick('世界地图', (-318, -100))

    if find_pic_inscreen('开始战斗'):
        find_pic_andclick('空白格子', (-295, 200), qianzhi=0, pause=0)
        find_pic_andclick('开始战斗', qianzhi=0, pause=0)
        pass


if __name__ == '__main__':
    while True:
        click_in_safe()
        click_in_safe()

        daigouliang()
