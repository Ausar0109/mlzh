from mlzhlc import *


def main(Nnum=100, timed=30, loopnumber=3):

    ccenter('action...!')

    ShangDian_SouSuo()
    get_in('julong')  # 选择
    loopmlzh(loopnumber)

    ccenter('循环检测时间 %s--%s' % (Nnum, timed))

    for ixy in range(Nnum):
        if isinstance(find_pic('yididenglu', timesleep=0), tuple):
            ccenter('检测到,给你六十分钟时间')
            time.sleep(50 * 60)
            ccenter('还剩10分钟....')
            time.sleep(10 * 60)
            login()

            break
        time.sleep(timed)
        click3(zbx['safewindow'])


if __name__ == '__main__':
    while True:
        main(80, 30, loopnumber=3)
