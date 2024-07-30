import time
from umqtt.simple import MQTTClient
import config

variables = {v: None for v in config.topics.values()}  # Ініціалізація змінних для зберігання значень

def message_callback(topic, msg):
    global variables
    topic_str = topic.decode('utf-8')
    msg_str = msg.decode('utf-8')
    print(f"Получено сообщение на тему {topic_str}: {msg_str}")
    
    if topic_str in config.topics:
        variable_name = config.topics[topic_str]
        variables[variable_name] = float(msg_str)
        print(f"update data {variable_name}: {variables[variable_name]}")
    else:
        print(f"unknown topic: {topic_str}")

def stop_condition():
    # Умови для завершення очікування повідомлень
    required_values = ['cur_temp', 'cur_temp_koll', 'temp_in', 'out_temp']
    return all(variables.get(value) is not None for value in required_values)

class MQTTConnector:
    def __init__(self, broker, port, username, password, client_id):
        self.broker = broker
        self.port = port
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client = MQTTClient(client_id, broker, port, username, password)

    def connect(self):
        print("Подключение к MQTT брокеру...")
        self.client.connect()
        print("Подключено к MQTT брокеру")

    def subscribe(self, topics, callback):
        self.client.set_callback(callback)
        for topic in topics:
            print(f"Подписка на тему: {topic}")
            self.client.subscribe(topic)

    def wait_for_message(self, wifi_connector, stop_condition):
        while True:
            if wifi_connector.is_connected():
                self.client.check_msg()
                time.sleep(1)
                # Проверка условия остановки ожидания сообщений
                if stop_condition():
                    print("Условие для остановки ожидания сообщений выполнено")
                    break
            else:
                print("Потеряно подключение к Wi-Fi. Ожидание восстановления...")
                time.sleep(2)

    def disconnect(self):
        self.client.disconnect()
        print("Отключено от MQTT брокера")
