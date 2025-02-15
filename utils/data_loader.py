import json
from utils.config_util import ConfigUtil
from models.test_data_model import TestData
from pydantic import ValidationError
import os


class DataLoader:

    @staticmethod
    def load_test_data(data_path=ConfigUtil.load_config().data_path):
        full_path = os.path.join(os.path.dirname(__file__), "..", data_path)
        with open(full_path, 'r', encoding="utf-8") as file:
            _data = json.load(file)
        try:
            validated_data = [TestData(**entry) for entry in _data]
            return validated_data
        except ValidationError as e:
            print("Ошибка валидации тестовых данных:", e)
            raise


