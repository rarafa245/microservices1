import time
from .mqtt_connection import registry_service_connection


def main():
    while True:
        time.sleep(0.001)
