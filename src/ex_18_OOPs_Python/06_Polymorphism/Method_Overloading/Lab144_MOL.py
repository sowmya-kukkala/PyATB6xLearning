class Browser:
    def make_http_request(self, url):
        print("Hi, Lets make the HTTP Request without Auth", url)

    def make_http_request(self, url, auth=None):
        print("Hi, Lets make the HTTP Request with Auth", url, auth)


req = Browser()
req.make_http_request("google.com") # Hi, Lets make the HTTP Request with Auth google.com None
req.make_http_request("google.com", "admin") # Hi, Lets make the HTTP Request with Auth google.com admin

