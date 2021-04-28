# -*- coding: utf-8 -*-

from json import dumps, loads
from string import Template

class JsonConfigError(Exception):
    pass

class JsonConfig:
    '''
    Read a JSON formatted configuration file
    '''
    def __init__(self, fname="config.json"):
        self.filename = fname
        self.config = None
    
    def read_configuration(self):
        try:
            with open(self.filename, 'r') as fh:
                content = fh.read()
                template = Template(content)
                config = template.safe_substitute(loads(content))
            self.config = loacs(config)
        except (IOError, OSError), err:
            msg = str(err)
            raise JsonConfigError(msg)
        except ValueError, err:
            msg = "{err}; possible syntax error in json file".format(err=str(err))
            raise JsonConfigErro(msg)
          
    def __str__(self):
        try:
            return dumps(self.config, indent=4)
        except:
            return "{}"
 
