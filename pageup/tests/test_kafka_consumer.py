import unittest
from pageup.kakfa import WebpageConsumer

class CustomError(Exception):
    pass

class MockKafkaConsumer:
    def __init__(self, topic, bootstrap_servers, **kwargs):
        self.receiveCalled = False
        self.server = bootstrap_servers

    def recieve(self, message):
        self.receiveCalled = True
    
class Test_Kafka_Consumer(unittest.TestCase):

    security = {"cafile":"test", "cert":"test", "key":"test"}

    def test_init_SSL(self):
        wc = WebpageConsumer("PageUp", protocol="SSL", data=self.security, kconsumer = MockKafkaConsumer)
        print(wc)
        self.assertEqual(wc.consumer.server,"localhost:9092")
        self.assertFalse(wc.consumer.receiveCalled)

    def test_init_nonSSL(self):
        wc = WebpageConsumer("PageUp", kconsumer = MockKafkaConsumer)
        self.assertEqual(wc.consumer.server,"localhost:9092")
        self.assertFalse(wc.consumer.receiveCalled)

    def test_init_error_SSL(self):
        with self.assertRaises(Exception):
            wc = WebpageConsumer("PageUp", protocol="SSL", kconsumer = MockKafkaConsumer)
            wc.consumer

    def test_write_called(self):
        wc = WebpageConsumer("PageUp", kconsumer = MockKafkaConsumer)
        self.assertFalse(wc.consumer.receiveCalled)

        