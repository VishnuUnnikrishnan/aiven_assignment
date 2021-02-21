#This module loads user defined settings from a json file
from . import log
from pathlib import Path
import json

class settings_functions:
    
    
    def __init__(self):
        try:
            with open("settings.json", "r") as f:
                settings = json.loads(f.read())
                self.settings = settings
        except:
            log.log_error("Settings.json can't be found","")                    

    
    '''Rather than having password in the source code, get it from a different location.
        This would be ideally from something like hashicorp's Vault or similar product rather
        than this which is from a hidden secrets folder.'''

    
    def getPassword(self, location):
        password = ""
        try:
            with open(location) as f:
                password = f.read()

        except Exception as e:
            log.log_error("Password file not found",e)
        return password
    
    def getSettings(self):
        return self.settings