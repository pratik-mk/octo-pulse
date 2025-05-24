import configparser
import os

class ConfParser:
    @staticmethod
    def get_config_value(key):
        broker = os.getenv("BROKER", "angel")
        print("Broker:", broker)
        config_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 
            "../../resources/config.ini",
        )
        config = configparser.ConfigParser()
        config.read(config_path)
        return config.get(broker, key)