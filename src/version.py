class BrowserVersion:
    version: str

    def get_version(self):
        return self.version
    
class Major(BrowserVersion):
    version = '1.0.0'

class Minor(BrowserVersion):
    version = '1.1.0'

class Build(BrowserVersion):
    version = '1.0.1'