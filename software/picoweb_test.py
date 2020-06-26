
import picoweb


def create_wifi():
    """创建网络"""
    import network
    ap_if = network.WLAN(network.AP_IF)
    print("init network ap mode")

    ap_if.active()  # 检查是否开启
    ap_if.active(True)  # 开启网络
    ap_if.config(essid='minicar')  # 设置AP热点你的名字
    ap_if.config(max_clients=3)  # 最大客户端数量
    ap_if.config(password='zlook119')  # 设置密码

    # 检查IP地址 会返回类似('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8')
    addr = ap_if.ifconfig()
    return addr


HOST = create_wifi()[0]  # 返回host
app = picoweb.WebApp(__name__)


@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("request success")


if __name__ == "__main__":
    app.run(debug=True, host=HOST)
