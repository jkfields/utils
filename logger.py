# -*- coding: utf-8 -*-

import logging
from logging.config import fileConfig
import os

DEFAULT_FORMAT = "%(asctime)s %(levelname)s [%(module)s %(funcName)s:%(lineno)d] - %(messages)s"
DEFAULT_DATEFMT = "%Y-%m-%dT%H:%M:%S"

def setup_logging(
    name: str = __name__, 
    format: str = DEFAULT_FORMAT,
    level: int = logging.DEBUG,
    dtformat : str = DEFAULT_DATEFMT
) -> logging.Logger:
    """
    Configure logging; if a config file (logging.ini) is not found in 
    the current directory, a default basic configuration is used
    """
    try:
        fileConfig('logging.ini')
    except:
        logging.basicConfig(format=format, level=level, datefmt=dtformat)
    finally:
        return logging.getLogger(__name__)
