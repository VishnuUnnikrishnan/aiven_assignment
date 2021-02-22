#! /usr/bin/python3
"""
This module reads from a kafka topic and
writes it to a postgres instance.
"""

from pageup.kakfa import WebpageConsumer
from pageup.database import dbwriter
from pageup.settings_class import settings_functions as Settings
import json

def main():
    config = Settings()
    settings = config.getSettings()

    consumer = None
    db = None

    #Support both SSL and non-SSL connections for local testing. 
    try:
        ssl_details = {"cafile":settings["KAFKA_CA_FILE"], "cert":settings["KAFKA_CERT_FILE"], "key":settings["KAFKA_KEY_FILE"]}
        consumer = WebpageConsumer(settings["KAFKA_TOPIC"], settings["KAFKA_SERVER"], settings["KAFKA_PORT"], 
                                   settings["KAFKA_CLIENT_ID"], settings["KAFKA_GROUP_ID"], 
                                   settings["KAFKA_PROTOCOL"], ssl_details)
    except:
        consumer = WebpageConsumer(settings["KAFKA_TOPIC"], settings["KAFKA_SERVER"], settings["KAFKA_PORT"], 
                                   settings["KAFKA_CLIENT_ID"], settings["KAFKA_GROUP_ID"])
    

    try:
        db = dbwriter(settings["DB_HOST"],settings["DB_PORT"], settings["DB_NAME"], 
                        settings["DB_USER"], config.getPassword(settings["DB_PASSWORD"]), settings["DB_TABLE"], settings["DB_PROTOCOL"])
    
    except:
        db = dbwriter(settings["DB_HOST"],settings["DB_PORT"], settings["DB_NAME"], 
                        settings["DB_USER"], config.getPassword(settings["DB_PASSWORD"]), settings["DB_TABLE"])

    if consumer is not None and db is not None:
        msgs = consumer.receive()
        for msg in msgs:
            db.write(msg)
    
        db.close
    


if __name__ == "__main__":
    main()