class BrowserName:
    name: str
    status: str = 'незапущенный'

    def get_name(self):
        return self.name
    
    def open_browser(self):
        self.status = 'открытый'

    def close_browser(self):
        self.status = 'закрытый'
    
    
class Mozilla(BrowserName):
    name = 'Mozilla'

class Chrome(BrowserName):
    name = 'Google Chrome'

class Yandex(BrowserName):
    name = 'Yandex'