#! /usr/bin/python3
"""
This module checks that a webpage is up and sends it
to a kafka topic.

"""

from pageup.web_connect import WebsiteCheck
from pageup.kakfa import WebpageProducer
from pageup.settings_class import settings_functions as Settings
import json

def main():
    config = Settings()
    settings = config.getSettings()
    wc = WebsiteCheck(url = settings["URL"], regex = settings["REGEX"] )
    pageUpDetails = wc.checkPage()
    producer = None
    

    #Support both SSL and non-SSL connections for local testing. 
    try:
        ssl_details = {"cafile":settings["KAFKA_CA_FILE"], "cert":settings["KAFKA_CERT_FILE"], "key":settings["KAFKA_KEY_FILE"]}
        producer = WebpageProducer(settings["KAFKA_TOPIC"], settings["KAFKA_SERVER"], settings["KAFKA_PORT"], settings["KAFKA_PROTOCOL"], ssl_details)
    except:
        producer = WebpageProducer(settings["KAFKA_TOPIC"], settings["KAFKA_SERVER"], settings["KAFKA_PORT"])
 
    if producer is not None:
        producer.send(json.dumps(pageUpDetails))

if __name__ == "__main__":
    main()
