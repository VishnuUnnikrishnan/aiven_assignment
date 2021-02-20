from helper_classes.kakfa import WebpageConsumer, WebpageProducer
from helper_classes.web_connect import WebsiteCheck
import settings
import json
import time

def main():
    
    wc = WebsiteCheck(url=settings.URL, regex=settings.REGEX)
    pageUpDetails = wc.checkPage()
    
    if pageUpDetails["error"] == False:
        producer = WebpageProducer()
        producer.send(json.dumps(pageUpDetails))

    else:
        pass

    time.sleep(1)

    consumer = WebpageConsumer()
    msgs = consumer.receive()
    print(msgs)
           
    

if __name__ == "__main__":
    # execute only if run as a script
    main()