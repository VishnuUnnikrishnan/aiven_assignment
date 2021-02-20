#This module setups logging to be used across application
#This module was developed based on code from:
#https://stackoverflow.com/questions/50391429/logging-in-classes-python

import logging
from datetime import datetime

logging.basicConfig(filename='logs/error.log',level=logging.ERROR)
logger = logging.getLogger('PageUpLogger')

def log_error(message, exceptions):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.error(time+" - "+message+"- Exception: "+str(exceptions))