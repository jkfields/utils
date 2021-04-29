# -*- coding: utf-8 -*-

import logging
from logging.config import fileConfig
import os

DEFAULT_FORMAT = "%(asctime)s %(levelname)s [%(module)s %(funcName)s:%(lineno)d] %(messages)s"
DEFAULT_DATEFMT = "%Y-%m-%dT%H:%M:%S"

'''
Configure logging; if a config file (logging.ini) is not found in the current directory, 
a default basic configuration is used
'''
try:
    fileConfig('logging.ini')
finally:
    logging.basicConfig(format=DEFAULT_FORMAT,
                        level=logging.DEBUG,
                        datefmt=DEFAULT_DATEFMT)

logger = loggiong.getLogger(__name__)
