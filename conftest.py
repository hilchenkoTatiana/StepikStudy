import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser...")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\n start firefox browser...")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n quit")
    browser.quit()
