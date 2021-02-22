import unittest
from pageup.kakfa import WebpageProducer

class CustomError(Exception):
    pass

class MockKafkaProducer:
    def __init__(self, bootstrap_servers, **kwargs):
        self.sendCalled = False
        self.server = bootstrap_servers

    def send(self, message):
        self.sendCalled = True
        if message =="Hello":
            return 1
        else:
            raise CustomError

class Test_Kafka_Producer(unittest.TestCase):

    security = {"cafile":"test", "cert":"test", "key":"test"}

    def test_init_SSL(self):
        wp = WebpageProducer(protocol="SSL", data=self.security, kproducer = MockKafkaProducer)
        self.assertEqual(wp.producer.server,"localhost:9092")
        self.assertFalse(wp.producer.sendCalled)

    def test_init_nonSSL(self):
        wp = WebpageProducer(kproducer = mockKafkaProducer)
        self.assertEqual(wp.producer.server,"localhost:9092")
        self.assertFalse(wp.producer.sendCalled)

    def test_init_error_SSL(self):
        with self.assertRaises(Exception):
            wp = WebpageProducer(protocol="SSL", kproducer = mockKafkaProducer)
            wp.producer

    def test_send(self):
        with self.assertRaises(Exception):
            wp = WebpageProducer(kproducer = mockKafkaProducer)
            self.assertEqual(wp.send("Hello"),1)
            self.assertTrue(wp.sendCalled)
            

    def test_send_error(self):
        
        with self.assertRaises(Exception):
            wp = WebpageProducer(kproducer = mockKafkaProducer)
            self.assertNotEqual(wp.send("Test"),1)
            self.assertTrue(wp.sendCalled)
   