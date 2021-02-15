import logging
import os
import pathlib
import sys


class CacheService:
    CACHE_DIR = pathlib.Path.home() / '.cvm' / 'cache'
    SETUP_DIR = pathlib.Path.home() / '.cvm' / 'setup'

    @staticmethod
    def boot_cache() -> None:
        home_directory = pathlib.Path.home()

        if not os.access(home_directory, os.W_OK) or not os.access(home_directory, os.X_OK):
            logging.error('Permission to home directory is required.')
            sys.exit(1)

        CacheService.CACHE_DIR.mkdir(parents=True, exist_ok=True)
        CacheService.SETUP_DIR.mkdir(parents=True, exist_ok=True)
        
    @staticmethod
    def make_cache_folder(folder: str) -> pathlib.Path:
        fpath = CacheService.CACHE_DIR / folder
        fpath.mkdir(parents=True, exist_ok=True)
        return fpath
