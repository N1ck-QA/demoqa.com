import os
import json
from models.config_model import Config


class ConfigUtil:

    @staticmethod
    def load_config(config_path="config/config.json"):
        full_path = os.path.join(os.path.dirname(__file__), "..", config_path)
        with open(full_path, 'r') as file:
            config = json.load(file)
        return Config(**config)
