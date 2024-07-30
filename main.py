from pid import PIDController
import config
import mqtt
from wifi_config import WiFiConnector
from mqtt import MQTTConnector, message_callback, stop_condition
import time

def main():
#     wifi_connector = WiFiConnector(config.SSID, config.PASSWORD)
#     mqtt_connector = MQTTConnector(config.mqtt_broker, config.mqtt_port, config.mqtt_username, config.mqtt_password, config.mqtt_client_id)
#     try:
#         wifi_connector.connect()
#         if wifi_connector.is_connected():
#             mqtt_connector.connect()
#             mqtt_connector.subscribe(list(config.topics.keys()), message_callback)
#             # Додаємо прапор завершення очікування повідомлення
#             mqtt_connector.wait_for_message(wifi_connector, stop_condition)
#         else:
#             print('WiFi не подключено. Повторная попытка через 2 секунд...')
#             time.sleep(2)
#     except Exception as e:
#         print(f'Ошибка: {e}')
#         time.sleep(5)
#     finally:
#         try:
#             mqtt_connector.disconnect()
#         except Exception as e:
#             print(f'Ошибка при отключении от MQTT: {e}')
#         try:
#             wifi_connector.disconnect()
#         except Exception as e:
#             print(f'Ошибка при отключении от Wi-Fi: {e}')
# 
#     # Використання збережених значень з variables
#     print(f'Используем сохраненные данные: {mqtt.variables}')
#     
    pid_controller = PIDController()

    # Запуск PID контролера
    print("Запуск PID контроллера")
    pid_controller.run()

if __name__ == "__main__":
    main()
