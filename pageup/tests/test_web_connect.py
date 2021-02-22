import unittest
from pageup.web_connect import WebsiteCheck

class MockElapsed:

    def total_seconds(self):
        return 0.5

class RequestsReturnObject:

    def __init__(self, status_code, elapsed, text):
        self.status_code = status_code
        self.elapsed = elapsed 
        self.text = text

class RequestsMock:

    def __init__(self, url="http://localhost", regex="", html_content = None):
        self.get_called = False
        self.url = url
        self.regex = regex
        self.html_content = html_content

    def get(self, url="", **kwargs):
        self.get_called = True
        if url == self.url:
            return RequestsReturnObject(200, MockElapsed(), self.html_content)
        else:
            raise Exception("Missing Server")

class TestWebsiteCheck(unittest.TestCase):
    def test_checkInit(self):
        requests_mock = RequestsMock()
        wc = WebsiteCheck("http://localhost","test",requests_mock)
        self.assertEqual(wc.url,"http://localhost")
        self.assertEqual(wc.regex,"test")
        self.assertEqual(wc.requestor,requests_mock)
        self.assertFalse(requests_mock.get_called)

    def test_CheckPage_MissingServer(self):
        requests_mock = RequestsMock()
        wc = WebsiteCheck("https://missingserver","test", requests_mock)
        test_data = wc.checkPage()
        self.assertTrue(requests_mock.get_called)
        self.assertEqual(test_data["status"], -1)
        self.assertEqual(test_data["error"], "Missing Server")
        self.assertEqual(test_data["elapsed"], -1)
        self.assertEqual(test_data["regex_found"], False)

    def test_CheckPage_ExistingServerRegexNotFound(self):
        requests_mock = RequestsMock(html_content="this is the content")
        wc = WebsiteCheck("http://localhost","test", requests_mock)
        test_data = wc.checkPage()
        self.assertTrue(requests_mock.get_called)
        self.assertEqual(test_data["status"], 200)
        self.assertEqual(test_data["error"], "")
        self.assertEqual(test_data["elapsed"], 0.5)
        self.assertEqual(test_data["regex_found"], False)
    
    def test_CheckPage_ExistingServerRegexFound(self):
        requests_mock = RequestsMock(html_content="test")
        wc = WebsiteCheck("http://localhost","test", requests_mock)
        test_data = wc.checkPage()
        self.assertTrue(requests_mock.get_called)
        self.assertEqual(test_data["status"], 200)
        self.assertEqual(test_data["error"], "")
        self.assertEqual(test_data["elapsed"], 0.5)
        self.assertEqual(test_data["regex_found"], True)