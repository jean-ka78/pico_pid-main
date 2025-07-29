# PID контролер конфігурація
SET_VALUE = 37.0
K_P = 0.025
K_I = 0.2
K_D = 1.1
CYCLE = 1.0
VALVE = 320.0
DEAD_ZONE = 2.0

# Піни реле та сенсора
RELAY_UP_PIN = 3
RELAY_DOWN_PIN = 4
SENSOR_PIN = 21

# Інші налаштування
ON_OFF = True
AUTO_HAND = True
HAND_UP = False
HAND_DOWN = False

# WIFI
SSID = 'aonline'
PASSWORD = '1qaz2wsx3edc'

# MQTT
mqtt_broker = 'greenhouse.net.ua'
mqtt_port = 1883
mqtt_username = 'mqtt'
mqtt_password = 'qwerty'
mqtt_client_id = 'pico_client'

# Словарь для хранения топиков и их соответствующих переменных
topics = {
    'home/heat_on/current-temperature/get': 'cur_temp',
    'home/heat_on/current-temperature_koll': 'cur_temp_koll',
    'home/esp-12f/current-temperature': 'temp_in',
    'home/pico/current_temperature': 'out_temp'
}
