import pytest
from itertools import product
from data23.version import *
from data23.name import *
from data23.browser import Browser

verions = [
    ('1.0.0', Major()),
    ('1.1.0', Minor()),
    ('1.0.1', Build()),
]

name_browsers = [
    ('Mozilla', Mozilla()),
    ('Google Chrome', Chrome()),
    ('Yandex', Yandex()),
]

cases = list(product(name_browsers, verions))

@pytest.mark.parametrize(argnames=['name_info', 'version_info'], argvalues=cases)
def test_not_running_browsers(name_info: tuple[str, BrowserName], version_info: tuple[str, BrowserVersion]) -> None:
    browser_name, browser = name_info
    version_name, version = version_info

    browser = Browser(browser, version)
    assert str(browser) == f'незапущенный {browser_name} браузер, версия {version_name}'