import unittest
from pageup.database import dbwriter

class MockCursor:
    
    def execute(self, **kwargs):
        pass

    def close(self):
        pass
    

class MockConnection:
    
    def cursor(self):
        return MockCursor()

    def commit(self):
        pass

    def close(self):
        pass


class MockDB:

    def __init__(**kwargs):
        self.write = False


    def connect(self):
        return MockConnection()

    def write(self, msg):
        self.write = True


class TestDatabase(unittest.TestCase):
    
    def test_init_SSL(self):
        writer = dbwriter(password ="test",protocol="SSL",pg=MockDB)
        self.assertEqual(writer.uri,"postgres://postgres:test@localhost:5432/pageup?sslmode=require")

    def test_init(self):
        writer = dbwriter(password ="test", pg=MockDB)
        self.assertEqual(writer.uri,"postgres://postgres:test@localhost:5432/pageup")

    def test_write(self):
        writer = dbwriter(password ="test", pg=MockDB)
        writer.write({"datetime":"2020-01-01 18:40:02", "status":"200", "elapsed":"0.2345", "regex_found":"True", "error":""})
        self.assertTrue(writer.write)

