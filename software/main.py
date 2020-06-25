
import picoweb
from motor import motor_dict


def create_wifi():
    """创建网络"""
    import network
    ap_if = network.WLAN(network.AP_IF)
    print("init network ap mode")

    ap_if.active()  # 检查是否开启
    ap_if.active(True)  # 开启网络
    ap_if.config(essid='minicar')  # 设置AP热点你的名字
    # 检查IP地址 会返回类似('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8')
    addr = ap_if.ifconfig()
    # ap_if.active(False)  # 禁用网络
    return addr


HOST = create_wifi()[0]  # 返回host
app = picoweb.WebApp(__name__)


@app.route("/")
def index(req, resp):
    # print("pos==>%s, speed==>%s" % (req.get("pos"), req.get("speed")))
    # 127.0.0.1:8088/?pos=0&speed=500   # pos范围是0-8 #speed范围500-1000
    req.parse_qs()  # 解析浏览器中传输的参数
    req_dict = req.form
    print("req_dict==>", req_dict, type(req_dict))

    msg = "resp"
    try:
        # 从参数中获取传递的参数
        pos = int(req_dict["pos"])
        speed = int(req_dict["speed"])

        if 8 >= pos >= 0 and 5 >= speed >= 1:  # 规范取值范围
            pass
        else:
            raise Exception("parse input error")

        msg = "minicar request success"
    except:
        pos, speed = 0, 0
        msg = "parse input error"

    # 进行pwm电机调速
    motor_dict[pos](speed*100 + 400)

    yield from picoweb.start_response(resp)
    yield from resp.awrite(msg)


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=8088)
