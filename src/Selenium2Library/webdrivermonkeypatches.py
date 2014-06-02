import time
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

class WebDriverMonkeyPatches:

    RemoteWebDriver._base_execute = RemoteWebDriver.execute

    def execute(self, driver_command, params=None):
        result = self._base_execute(driver_command, params)
        speed = self._get_speed()
        if speed > 0:
            time.sleep(speed)
        return result

    def get_current_url(self):
        return self.current_url

    def get_current_window_handle(self):
        return self.current_window_handle

    def get_current_window_info(self):
        atts = self.execute_script("return [ window.id, window.name, document.title, document.url ];")
        atts = [ att if att is not None and len(att) else 'undefined'
            for att in atts ]
        return (self.current_window_handle, atts[0], atts[1], atts[2], atts[3])

    def get_page_source(self):
        return self.page_source

    def get_title(self):
        return self.title

    def get_window_handles(self):
        return self.window_handles

    def current_window_is_main(self):
        return self.current_window_handle == self.window_handles[0];

    def set_speed(self, seconds):
        self._speed = seconds

    def _get_speed(self):
        if not hasattr(self, '_speed'):
            self._speed = float(0)
        return self._speed

    RemoteWebDriver.get_title = get_title
    RemoteWebDriver.get_current_url = get_current_url
    RemoteWebDriver.get_page_source = get_page_source
    RemoteWebDriver.get_current_window_handle = get_current_window_handle
    RemoteWebDriver.get_current_window_info = get_current_window_info
    RemoteWebDriver.get_window_handles = get_window_handles
    RemoteWebDriver.set_speed = set_speed
    RemoteWebDriver._get_speed = _get_speed
    RemoteWebDriver.execute = execute
