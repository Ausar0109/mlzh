from mlzhlc import *


def main(Nnum=100, timed=30, loopnumber=3):

    ccenter('action...!')

    ShangDian_SouSuo()
    get_in('julong')  # 选择
    loopmlzh(loopnumber)

    ccenter('循环检测时间 %s--%s' % (Nnum, timed))

    for ixy in range(Nnum):
        if isinstance(find_pic('yididenglu', timesleep=0), tuple):
            ccenter('检测到,给你三十分钟时间')
            time.sleep(30 * 60)
            login()

            if Nnum - ixy - 65 > 0:
                ccenter('检测时间剩余 %s--%s' % ((Nnum - ixy - 30), timed))
                time.sleep((Nnum - ixy - 65) * timed)
            else:
                ccenter('无剩余时间')

            break
        time.sleep(timed)


if __name__ == '__main__':
    while True:
        main(80, 30, loopnumber=3)
