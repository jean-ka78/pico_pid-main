import network
import time

class WiFiConnector:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self):
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)
        max_wait = 10
        while max_wait > 0:
            if self.wlan.status() < 0 or self.wlan.status() >= 3:
                break
            max_wait -= 1
            print('Подключение...к сети Wi-Fi')
            print(f'Connecting to {self.ssid}...')
            time.sleep(3)

        if self.wlan.status() != 3:
            print('Не удалось подключиться к сети Wi-Fi')
        else:
            print('Подключено')
            status = self.wlan.ifconfig()
            print('ip = ' + status[0])

    def disconnect(self):
        self.wlan.disconnect()
        self.wlan.active(False)
        print('Отключено от Wi-Fi')

    def is_connected(self):
        return self.wlan.isconnected()
