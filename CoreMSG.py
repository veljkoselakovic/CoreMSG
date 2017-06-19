import selenium
import time
import json
import pickle


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CoreMSG(object):
    #emoji = json.load(open('emojis.txt'))
    #emoji_s = json.load(open('emojis_standard.txt'))

    def __init__(self, email, passwd):
        self.email = email
        self.passwd = passwd

    def login_messenger(self, driver):
        try:
            for cookie in pickle.load(open("Cookies.pkl", "rb")):
                driver.add_cookie(cookie)
            driver.refresh()
            time.sleep(4)

        except:

            username = driver.find_element_by_id("email")
            password = driver.find_element_by_id("pass")

            username.send_keys(self.email)
            password.send_keys(self.passwd)
            driver.find_element_by_name("login").click()
            time.sleep(4)
            # login code
            pickle.dump(driver.get_cookies(), open("Cookies.pkl","wb"))

    def msg_attempt(self, driver, text):
        textbox = driver.find_element_by_class_name('_5rpu')
        textbox.send_keys(text)
        textbox.send_keys(Keys.ENTER)

    def change_emoji(self, emoji_code, target, aftertext = 'aftertext'):
        driver = selenium.webdriver.PhantomJS()
        driver.get('https://www.messenger.com/t/' + target)
        assert "Messenger" in driver.title
        self.login_messenger(driver)
        time.sleep(3)

        driver.execute_script("document.querySelectorAll('._3szq')[3].click()")
        time.sleep(3)
        driver.find_elements_by_class_name(' _4rlu')[emoji_code].click()

        if aftertext != 'aftertext' or not aftertext:
            self.msg_attempt(driver, aftertext)

        assert "No results found." not in driver.page_source
        driver.close()
    def change_color(self, color_code, target, aftertext = 'aftertext'):
            driver = selenium.webdriver.PhantomJS()
            driver.get('https://www.messenger.com/t/' + target)
            assert "Messenger" in driver.title
            self.login_messenger(driver)
            time.sleep(3)

            driver.execute_script("document.querySelectorAll('._3szq')[2].click()")
            time.sleep(3)
            driver.find_elements_by_class_name(' _5dr4')[color_code].click()

            if aftertext != 'aftertext' or not aftertext:
                self.msg_attempt(driver, aftertext)

            assert "No results found." not in driver.page_source
            driver.close()
    def send_msg_fb(self, text, target):
        driver = selenium.webdriver.PhantomJS()
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

        print("DONE")

#  API