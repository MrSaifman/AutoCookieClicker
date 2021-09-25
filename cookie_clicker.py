from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = "chromedriver.exe"
URL = "https://orteil.dashnet.org/cookieclicker/"


class CookieClicker():
    def __init__(self):
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.driver.get(URL)
        self.cookie = self.driver.find_element_by_id("bigCookie")
        
        self.shop = {
            "Cursor": "15",
            "Grandma": "100",
            "Farm": "1100",
            "Mine": "12000",
            "Factory": "130000"
            "https://cookieclicker.fandom.com/wiki/Building"
        }
        self.click_loop()

    
    def click_loop(self):
        while True:
            self.cookie.click()
            self.get_cookies()
    
    def get_cookies(self):
        cookies_element = self.driver.find_element_by_id("cookies")
        cookies_text = cookies_element.text
        cookies = cookies_text.split(' ')[0]
        cookies = cookies.replace(',', '')
        print(cookies)



if __name__ == '__main__':
    app = CookieClicker()
