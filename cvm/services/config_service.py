import json
import pathlib


class ConfigService:
    FILENAME = '.cvm_config'
    CONFIG_INPUT = pathlib.Path(FILENAME)

    @staticmethod
    def exists() -> bool:
        return ConfigService.CONFIG_INPUT.exists()

    @staticmethod
    def read():
        return json.load(ConfigService.CONFIG_INPUT.open('r'))

    @staticmethod
    def validate(data) -> bool:
        if 'requires' not in data:
            return False
        return True
