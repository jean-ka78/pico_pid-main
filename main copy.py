from pid import PIDController
import config
from wifi_config import WiFiConnector
from mqtt import MQTTConnector
from mqtt import message_callback
import time

def main():
    # Підключення до Wi-Fi
    #wifi_config.connect_wifi(wifi_config.SSID, wifi_config.PASSWORD)
    #wifi_connector = WiFiConnector(config.SSID, config.PASSWORD)
    #mqtt_connector = MQTTConnector(config.mqtt_broker, config.mqtt_port, config.mqtt_username, config.mqtt_password, config.mqtt_client_id)
    #wifi_connector.connect()
    wifi_connector = WiFiConnector(config.SSID, config.PASSWORD)
    mqtt_connector = MQTTConnector(config.mqtt_broker, config.mqtt_port, config.mqtt_username, config.mqtt_password, config.mqtt_client_id)
    try:
        wifi_connector.connect()
        if wifi_connector.is_connected():
            mqtt_connector.connect()
            mqtt_connector.subscribe(list(config.topics.keys()), message_callback)
            mqtt_connector.wait_for_message(wifi_connector)
        else:
            print('WiFi не подключено. Повторная попытка через 2 секунд...')
            time.sleep(2)
    except Exception as e:
        print(f'Ошибка: {e}')
        time.sleep(5)
    finally:
        try:
            mqtt_connector.disconnect()
        except:
            pass
        wifi_connector.disconnect()

    # В цьому місці можна використовувати збережені значення з variables
    print(f'Используем сохраненные данные: {variables}')
    
    
    pid_controller = PIDController()

    # Запуск PID контролера
    pid_controller.run()
    #time.sleep(1)
    # Ініціалізація PID контролера
#     while True:
#         wifi_connector = WiFiConnector(config.SSID, config.PASSWORD)
#         mqtt_connector = MQTTConnector(config.mqtt_broker, config.mqtt_port, config.mqtt_username, config.mqtt_password, config.mqtt_client_id)
# 
#         try:
#             wifi_connector.connect()
#             if wifi_connector.is_connected():
#                 mqtt_connector.connect()
#                 mqtt_connector.subscribe(list(config.topics.keys()), message_callback)
#                 mqtt_connector.wait_for_message(wifi_connector)
#             else:
#                 print('WiFi не подключено. Повторная попытка через 2 секунд...')
#                 time.sleep(2)
#         except Exception as e:
#             print(f'Ошибка: {e}')
#             time.sleep(5)
#         finally:
#             try:
#                 mqtt_connector.disconnect()
#             except:
#                 pass
#             wifi_connector.disconnect()

    # В цьому місці можна використовувати збережені значення з variables
#     print(f'Используем сохраненные данные: {variables}')
   
    

if __name__ == "__main__":
    main()
