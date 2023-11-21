from pytest import mark, Metafunc
from itertools import product
from src.version import *
from src.name import *
from src.browser import Browser


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

def pytest_generate_tests(metafunc: Metafunc) -> None:
    cases = []
    test_names = []
    for case in product(name_browsers, verions):
        name_info, version_info = case
        browser_name, browser = name_info
        version_name, version = version_info
        cases.append([browser_name, browser, version_name, version])
        test_names.append(f'{browser_name} - {version_name}')

    metafunc.parametrize(argnames=['browser_name', 'browser', 'version_name', 'version'], argvalues=cases, ids=test_names)


def test_not_running_browsers(browser_name: str, browser: BrowserName, version_name: str, version: BrowserVersion) -> None:
    inst_browser = Browser(browser, version)
    assert str(inst_browser) == f'незапущенный {browser_name} браузер, версия {version_name}'


def test_running_browsers(browser_name: str, browser: BrowserName, version_name: str, version: BrowserVersion) -> None:
    inst_browser = Browser(browser, version)
    inst_browser.run_browser()
    assert str(inst_browser) == f'открытый {browser_name} браузер, версия {version_name}'


def test_not_running_browsers(browser_name: str, browser: BrowserName, version_name: str, version: BrowserVersion) -> None:
    inst_browser = Browser(browser, version)
    inst_browser.run_browser()
    inst_browser.terminate_browser()
    assert str(inst_browser) == f'закрытый {browser_name} браузер, версия {version_name}'