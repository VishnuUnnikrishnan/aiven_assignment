from datetime import datetime
import requests
import re

# This class handles checking a website to see if its up
class  WebsiteCheck:

    def __init__(self, url="http://localhost", regex=""):
        self.url = url
        self.regex = regex
    
    #This function checks if the provided webpage is available.
    def checkPage(self):
        details = {}
        details["datetime"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            r = requests.get(self.url, timeout = 1)
            details["error"] = ""
            details["status"] = r.status_code
            details["elapsed"] = r.elapsed.total_seconds()
            details["regex_found"] = self.__regexCheck(r.text)

        except Exception as e:
            details["error"] = str(e)
            details["status"] = -1
            details["elapsed"] = -1
            details["regex_found"] = False

        return details
    
    #This function checks if the webpage has a defined regex pattern
    def __regexCheck(self, html):
        try:
            re.search(self.regex, html)
            return True
        except:
            return False

def main():
    wc = WebsiteCheck()
    print(wc.checkPage())


if __name__ == "__main__":
    # execute only if run as a script
    main()