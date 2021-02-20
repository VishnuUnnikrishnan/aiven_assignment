# consumer and producer code based on: 
# https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka


from kafka import KafkaProducer, KafkaConsumer
from pathlib import Path
from . import log
import json

#This is the specific producer class. 
class WebpageProducer:
    def __init__(self, topic="PageUp", server="localhost", port=9092, protocol=None, data=None):
        
        try:
            self.topic = topic
            if protocol == None:
                producer = KafkaProducer(bootstrap_servers = server+":"+str(port))

            elif protocol == "SSL":
                producer = KafkaProducer(bootstrap_servers = server+":"+str(port),
                                     security_protocol = protocol,
                                     ssl_cafile=data["cafile"],
                                     ssl_certfile=data["cert"],
                                     ssl_keyfile=data["key"],
                                    )

            else:
                log.log_error("Unable to create producer", "Protocol not supported")                       
            #add more protocols here if required eg. support for SASL

            self.producer = producer 

        except Exception as e:
            log.log_error("Unable to create producer", e)

    def send(self, message):
        try:
            self.producer.send(self.topic, message.encode("utf-8"))        
        except Exception as e:
            log.log_error("Unable to send data to Kafka", e)


#This is the specific consumer class
class WebpageConsumer:
    def __init__(self, topic="PageUp", server="localhost", port=9092, protocol=None, data=None,client_id="demo", group_id="demo"): 
        try:
            if protocol == None:
                consumer = KafkaConsumer(topic,
                                         bootstrap_servers = server+":"+str(port),
                                         client_id=client_id,
                                         group_id=group_id,
                                         auto_offset_reset="earliest",
                                        )
            elif protocol == "SSL":
                consumer = KafkaConsumer(topic,
                                         bootstrap_servers = server+":"+str(port),
                                         client_id=client_id,
                                         group_id=group_id,
                                         auto_offset_reset="earliest",
                                         security_protocol = protocol,
                                         ssl_cafile=data["cafile"],
                                         ssl_certfile=data["cert"],
                                         ssl_keyfile=data["key"],
                                        )
            else:
                log.log_error("Unable to create consumer", "Protocol not supported") 

            self.consumer = consumer

        except Exception as e:
            log.log_error("Unable to create consumer", e)
    
    def receive(self):
        data = []
        try:
            for _ in range(2):
                raw_msgs = self.consumer.poll(timeout_ms=1000)
                for msgs in raw_msgs.items():
                    for msg in msgs[1]:
                        data.append(json.loads(msg.value))
            self.consumer.commit()

        except Exception as e:
            log.log_error("Unable to recieve data from Kafka", e)
        
        return data


def main():
    pass

if __name__ == "__main__":
    # execute only if run as a script
    main()