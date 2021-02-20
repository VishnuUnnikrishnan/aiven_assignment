from helper_classes.kakfa import WebpageConsumer, WebpageProducer
from helper_classes.web_connect import WebsiteCheck
from helper_classes.database import dbwriter
import settings
import json
import time

def main():
    
    wc = WebsiteCheck(url=settings.URL, regex=settings.REGEX)
    pageUpDetails = wc.checkPage()
    
    if pageUpDetails["error"] == "":
        producer = WebpageProducer()
        producer.send(json.dumps(pageUpDetails))

    else:
        pass

    time.sleep(1)

    consumer = WebpageConsumer()
    msgs = consumer.receive()
    
    db = dbwriter()
    
    for msg in msgs:
        db.write(msg)
    
    db.close
    
if __name__ == "__main__":
    # execute only if run as a script
    main()