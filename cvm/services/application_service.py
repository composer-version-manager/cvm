import json
import logging
import os
import subprocess
import re
import pathlib
import sys
from enum import Enum
from typing import Any, Optional


class ComposerSource(Enum):
    Empty = ''
    Global = 'global'
    Config = 'config'

class ApplicationService:
    APP_DIR = pathlib.Path.home() / '.cvm'
    APP_FILE_PATH = APP_DIR / 'config.json'

    def __init__(self):
        ApplicationService.APP_DIR.mkdir(parents=True, exist_ok=True)
        ApplicationService.APP_FILE_PATH.touch(exist_ok=True)
        self._parse()

    def get_updated_path(self, bin_path: str) -> str:
        envPath = self._get_env_path()
        clean_path = self._clean_env_path(envPath)
        updated_path = f"{bin_path}:{clean_path}"
        
        return updated_path

    def _clean_env_path(self, envPath: str) -> str:
        return re.sub(r'\/(\b[^:]+)\/.cvm\/cache\/.+?(:|$)', '', envPath)

    def _get_env_path(self) -> str:
        return subprocess.check_output("echo $PATH", shell=True).decode('ascii')

    def _parse(self):
        try:
            self._app = json.load(ApplicationService.APP_FILE_PATH.open('r'))
        except:
            self._app = {}

        if not self._app:
            self._app = {
                'global': None,
                'current': None,
                'source': str(ComposerSource.Empty),
            }
            self._write()

    def _write(self):
        ApplicationService.APP_FILE_PATH.write_text(json.dumps(self._app))

    def app(self) -> dict:
        return self._app

    def get(self, key: str) -> Any:
        return self._app.get(key)

    def set(self, key: str, value: Any):
        if type(value) is ComposerSource:
            value = str(value)

        self._app[key] = value

    def save(self):
        self._write()
