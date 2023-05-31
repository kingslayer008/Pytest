import time

import pytest
from selenium.webdriver.common.by import By

from utilities.WebdriverFactory import WebDriverFactory
from config import Config

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    wd = WebDriverFactory()
    driver = wd.webdriverreturn(browser_name)
    request.cls.driver = driver
    driver.get(Config.get_url())
    driver.maximize_window()
    driver.implicitly_wait(10)
    try:
        login()
    except Exception as e:
        print(e)

    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


def login():
    driver.find_element(By.ID, "username").send_keys(Config.get_username())
    driver.find_element(By.ID, "password").send_keys(Config.get_password())
    driver.find_element(By.ID, "signInBtn").click()
    time.sleep(3)


