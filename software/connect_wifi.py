import network


def connect():
    ssid = "zlook"
    password = "zlllllll"
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Already connected")
        return
    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        print("Connection successful")
        print(station.ifconfig())


if __name__ == '__main__':
    connect()
