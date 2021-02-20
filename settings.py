#This file holds constants like file paths etc. Change here to modify 
# parameters for the application. 
import helper_classes.log as log
from pathlib import Path

'''Rather than having password in the source code, get it from a different location.
This would be ideally from something like hashicorp's Vault or similar product rather
than this which is from a hidden secrets folder.'''

def getPassword(location):
    password = ""
    try:
        with open(SECRETS_PATH+location) as f:
            password = f.read()

    except Exception as e:
        log.log_error("Password file not found",e)
    return password  



#WebPage details
URL = "https://www.google.com"
REGEX = ""

#Kafka instance details
SERVER = ""
PORT = 9092

TOPIC = "PageUp"
PROTOCOL = "SSL"
SECRETS_PATH = str(Path(__file__).resolve().parents[0])+"/.secrets/"
CA_FILE = SECRETS_PATH+"ca.pem"
CERT_FILE = SECRETS_PATH+"service.cert"
KEY_FILE = SECRETS_PATH+"service.key"

#Database details

DB_NAME = "PageUp"
DB_USER = "tempadmin"
DB_PASSWORD = getPassword("dbpass")
DB_PORT = 5432
DB_PROTOCOL = "SSL"

  