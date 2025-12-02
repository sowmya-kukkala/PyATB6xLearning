from abc import ABC, abstractmethod
from webbrowser import Chrome


class BrowserManager(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Stop Command")

class ChromeBrowser(BrowserManager):
    def start(self):
        # t = ChromeDriver() -> Like this we can write our code here
        print("We are starting the Chrome")

tc = ChromeBrowser()
tc.start() # We are starting the Chrome
tc.stop() # Stop Command



