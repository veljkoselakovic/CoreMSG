import selenium
import time
import json


from cookies import Cookies
from selenium.webdriver.common.keys import Keys


class CoreMSG(object):
    emoji = json.load(open('emojis.txt'))
    emoji_s = json.load(open('emojis_standard.txt'))

    def __init__(self, email, passwd):
        self.email = email
        self.passwd = passwd

    def login_messenger(self, driver):
        msg_driver = Cookies(driver)
        try:
            msg_driver.get_cookies()
            driver.refresh()
            time.sleep(4)

        except EOFError:
            username = driver.find_element_by_id("email")
            password = driver.find_element_by_id("pass")

            username.send_keys(self.email)
            password.send_keys(self.passwd)
            driver.find_element_by_name("login").click()
            time.sleep(4)
            msg_driver.log_cookies()

    def msg_attempt(self, driver, text):
        textbox = driver.find_element_by_class_name('_5rpu')
        textbox.send_keys(text)
        textbox.send_keys(Keys.ENTER)

    def change_emoji(self, emoji_code, target, aftertext = 'aftertext'):
        driver = selenium.webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
        driver.get('https://www.messenger.com/t/' + target)
        assert "Messenger" in driver.title
        self.login_messenger(driver)
        time.sleep(3)

        driver.execute_script("document.querySelectorAll('._3szq')[2].click()")
        time.sleep(3)
        driver.find_elements_by_class_name(' _4rlu')[emoji_code].click()

        if aftertext != 'aftertext' or not aftertext:
            self.msg_attempt(driver, aftertext)

        assert "No results found." not in driver.page_source
        driver.close()

    def send_msg_fb(self, text, target):
        driver = selenium.webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
        #driver.manage().window().setPosition(new Point(-2000, 0))
        driver.get('https://www.messenger.com/t/' + target)
        assert "Messenger" in driver.title

        self.login_messenger(driver)
        time.sleep(3)
        #driver.refresh()
        #time.sleep(3)
        self.msg_attempt(driver, text)

        assert "No results found." not in driver.page_source
        driver.close()

#  API
