import sys

MIN_PYTHON = (3, 0)


def check_minimum_version():
    if sys.version_info < MIN_PYTHON:
        sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)


from src.app import bootstrap

bootstrap.run()
