from machine import Pin, PWM


p25 = PWM(Pin(25), freq=20000, duty=0)  # 右前轮
p26 = PWM(Pin(26), freq=20000, duty=0)  # 左前轮
p27 = PWM(Pin(27), freq=20000, duty=0)  # 右后轮
p14 = PWM(Pin(14), freq=20000, duty=0)  # 左后轮

# duty 范围 500-1000


def up(speed):
    """前进"""
    p25.duty(speed)
    p26.duty(speed)
    p27.duty(0)
    p14.duty(0)


def down(speed):
    """后退"""
    p25.duty(0)
    p26.duty(0)
    p27.duty(speed)
    p14.duty(speed)


def left(speed):
    """左转"""
    p25.duty(speed)
    p26.duty(0)
    p27.duty(0)
    p14.duty(0)


def right(speed):
    """右转"""
    p25.duty(0)
    p26.duty(speed)
    p27.duty(0)
    p14.duty(0)


def up_left(speed):
    """左前"""
    p25.duty(speed)
    p26.duty(1000 - speed)
    p27.duty(0)
    p14.duty(0)


def up_right(speed):
    """右前"""
    p25.duty(1000 - speed)
    p26.duty(speed)
    p27.duty(0)
    p14.duty(0)


def down_left(speed):
    """左后"""
    p25.duty(0)
    p26.duty(0)
    p27.duty(1000-speed)
    p14.duty(speed)


def down_right(speed):
    """右后"""
    p25.duty(0)
    p26.duty(0)
    p27.duty(speed)
    p14.duty(1000 - speed)


def stop(speed):
    """停止"""
    p25.duty(0)
    p26.duty(0)
    p27.duty(0)
    p14.duty(0)


motor_dict = {
    0: stop,
    1: up,
    2: down,
    3: left,
    4: right,
    5: up_left,
    6: up_right,
    7: down_left,
    8: down_right
}
