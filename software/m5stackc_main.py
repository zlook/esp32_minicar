from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import imu
from time import sleep_ms
from math import fabs as abs
import urequests

setScreenColor(0x111111)


imu0 = imu.IMU()

wifiCfg.screenShow()
wifiCfg.autoConnect(lcdShow=True)
wifiCfg.doConnect('minicar', None)

setScreenColor(0x3797de)
label1 = M5TextBox(15, 140, "x:", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=270)
label0 = M5TextBox(15, 115, "Text", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=270)

label2 = M5TextBox(45, 140, "y:", lcd.FONT_DejaVu18, 0xf10909, rotate=270)
label4 = M5TextBox(45, 115, "Text", lcd.FONT_DejaVu18, 0xf10909, rotate=270)


label3 = M5TextBox(18, 65, "STATE", lcd.FONT_DejaVu18, 0xf10909, rotate=270)
status = M5TextBox(42, 65, "S", lcd.FONT_DejaVu18, 0x009900, rotate=270)

stop_limit = 10  # 当范围为limit默认为停止

status_dict = {
    0: "S",
    1: "U",
    2: "D",
    3: "L",
    4: "R",
    5: "UL",
    6: "UR",
    7: "DL",
    8: "DR"
}

while True:
    x = int(imu0.ypr[2])
    y = int(imu0.ypr[1])
    if x >= 60:
        x = 60
    if x <= -60:
        x = -60
    if y >= 60:
        y = 60
    if y <= -60:
        y = -60

    label0.setText("%s" % x)
    label4.setText("%s" % y)

    # 计算出速度
    speed_max = max(abs(x), abs(y)) - stop_limit
    speed = int(abs(speed_max // 10))

    pos = 0  # 赋初始值
    # 停止
    if abs(x) <= stop_limit and abs(y) <= stop_limit:
        pos = 0

    # 前进
    if x < -stop_limit and -stop_limit < y < stop_limit:
        pos = 1

    # 后退
    if x > stop_limit and - stop_limit < y < stop_limit:
        pos = 2

    # 左转
    if -stop_limit <= x <= stop_limit and y > stop_limit:
        pos = 3

    # 右转
    if -stop_limit <= x <= stop_limit and y < -stop_limit:
        pos = 4

    # 左前
    if (x < -stop_limit) and (y >= stop_limit):
        pos = 5

    # 右前
    if (x < -stop_limit) and (y <= -stop_limit):
        pos = 6

    # 左后
    if (x > stop_limit) and (y >= stop_limit):
        pos = 7

    # 右后
    if (x > stop_limit) and (y <= -stop_limit):
        pos = 8

    status_lab = status_dict[pos]
    status.setText("%s->%s" % (status_lab, speed))

    try:
        req = urequests.request(
            method='GET', url='http://192.168.4.1:8088/?pos=%s&speed=%s' % (pos, speed))
    except:
        setScreenColor(0xff0000)

    sleep_ms(500)
