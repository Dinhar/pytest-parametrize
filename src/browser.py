from src.name import BrowserName
from src.version import BrowserVersion

class Browser:
    name: BrowserName
    version: BrowserVersion

    def __init__(self, name: BrowserName, version: BrowserVersion):
        self.name = name
        self.version = version

    def __str__(self):
        return f'{self.name.status} {self.name.get_name()} браузер, версия {self.version.get_version()}'

    def __repr__(self):
        return str(self)
    
    def run_browser(self):
        self.name.open_browser()

    def terminate_browser(self):
        self.name.close_browser()
