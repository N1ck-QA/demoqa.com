from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.config_util import ConfigUtil


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class WebDriver(metaclass=Singleton):
    _driver = None

    @property
    def driver(self):
        if self._driver is None:
            browser = ConfigUtil.load_config().browser
            if browser == 'chrome':
                self._driver = self._create_chrome_driver()
            elif browser == 'firefox':
                self._driver = self._create_firefox_driver()
            else:
                raise ValueError(f"Неизвестный браузер: {browser}")
        return self._driver

    @staticmethod
    def _create_chrome_driver():
        options = ChromeOptions()
        if ConfigUtil.load_config().browser_options.window_size:
            options.add_argument(ConfigUtil.load_config().browser_options.window_size)
        if ConfigUtil.load_config().browser_options.incognito:
            options.add_argument("--incognito")
        return webdriver.Chrome(options=options)

    @staticmethod
    def _create_firefox_driver():
        options = FirefoxOptions()
        if ConfigUtil.load_config().browser_options.incognito:
            options.set_preference("browser.privatebrowsing.autostart", True)
        firefox_driver = webdriver.Firefox(options=options)
        if ConfigUtil.load_config().browser_options.window_size:
            firefox_driver.fullscreen_window()
        return firefox_driver

    def quit_driver(self):
        if self._driver:
            self._driver.quit()
            WebDriver._driver = None
            WebDriver._instances.pop(WebDriver, None)
