import json
import pathlib
from typing import Optional

from cvm.helpers.fs import find_file_in_parent


class ConfigService:
    FILENAME = '.cvm_config'
    CONFIG_INPUT = pathlib.Path(FILENAME)

    @staticmethod
    def exists() -> bool:
        return ConfigService.CONFIG_INPUT.exists()

    @staticmethod
    def find() -> Optional[pathlib.Path]:
        return find_file_in_parent(ConfigService.FILENAME, recursive=True)

    @staticmethod
    def read(config_file: pathlib.Path):
        return json.load(config_file.open('r'))

    @staticmethod
    def validate(data) -> bool:
        if 'requires' not in data:
            return False
        return True
