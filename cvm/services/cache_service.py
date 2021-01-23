import os
import logging
import sys
from pathlib import Path


class CacheService:
    CACHE_DIR = os.path.expanduser('~') + '/.cvm/cache'

    @staticmethod
    def boot_cache():
        home_directory = os.path.expanduser('~')

        if not os.access(home_directory, os.W_OK) or not os.access(home_directory, os.X_OK):
            logging.error('Permission to home directory is required.')
            sys.exit(1)

        if not os.path.exists(CacheService.CACHE_DIR):
            Path(CacheService.CACHE_DIR).mkdir(parents=True, exist_ok=True)
