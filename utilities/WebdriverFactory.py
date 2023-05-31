
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class WebDriverFactory:
    def webdriverreturn(self, browser_name):
        if browser_name == "chrome":
            options = Options()
            #options.add_argument("--headless")
            options.add_argument("--disable-extensions")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument(f"--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        elif browser_name == "firefox":
            driver = webdriver.Firefox(GeckoDriverManager().install())
        elif browser_name == "IE":
            print("IE driver")
        return driver
