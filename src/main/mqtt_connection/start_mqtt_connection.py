from .client_config import mqtt_client_config
from .mqtt_client import MqttClient

registry_service_connection = MqttClient(
    mqtt_client_config["HOST"],
    mqtt_client_config["PORT"],
    mqtt_client_config["CLIENT_NAME"],
    mqtt_client_config["KEEPALIVE"],
)
