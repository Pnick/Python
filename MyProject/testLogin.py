from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from commonWebDriver import *

class LoginTests(TestCase):

    def test_1_login_without_username_and_pass(self):
        self.driver = DRIVER

        user_present = EC.presence_of_element_located((By.NAME , 'user'))
        WebDriverWait(self.driver, 6).until(user_present)
        
        user = self.driver.find_element_by_name("user")
        user.send_keys(userName)
        print("\nPreconditions: Set string: '" + userName + "' into username field")
        user.clear()
        print("Test action: Clear username field")
        passw = self.driver.find_element_by_name("pass")
        passw.clear()
        print("Test action: Clear password field")
        passw.send_keys(Keys.RETURN)
        print("Test action: Click ENTER button")
        assert "Попълнете правилно и двете полета" in self.driver.page_source
        print("Test result: Login page is displayed and message: 'Попълнете правилно и двете полета'")
      
    def test_2_login_without_username(self):
        self.driver = DRIVER
        user = self.driver.find_element_by_name("user")
        user.clear()
        print("\nTest action: Clear username field")
        passw = self.driver.find_element_by_name("pass")
        passw.send_keys("tralalala123!")
        print("Test action: Set incorrect string into password field")
        passw.send_keys(Keys.RETURN)
        print("Test action: Click ENTER button")
        assert "Не сте въвели адрес" in self.driver.page_source
        print("Test result: Login page is displayed and message: 'Не сте въвели адрес'")

    def test_3_login_without_pass(self):
        self.driver = DRIVER
        user = self.driver.find_element_by_name("user")
        user.send_keys(userName)
        print("\nTest action: Set correct string: '" + userName + "' into username field")
        passw = self.driver.find_element_by_name("pass")
        passw.clear()
        print("Test action: Clear password field")
        passw.send_keys(Keys.RETURN)
        print("Test action: Click ENTER button")
        assert "Не сте въвели парола" in self.driver.page_source
        print("Test result: Login page is displayed and message: 'Не сте въвели парола'")

    def test_4_login_wrong_pass(self):
        self.driver = DRIVER
        user = self.driver.find_element_by_name("user")
        user.send_keys(userName)
        print("\nTest action: Set correct string: '" + userName + "' into username field")
        passw = self.driver.find_element_by_name("pass")
        passw.send_keys("alabalahjhgkjkkkhkjhjhkjhkjhkjhalabalahjhgkjkkkhkjhjhkjhkjhkjhalabalahjhgkjkkkhkjhjhkjhkjhkjh")
        print("Test action: Set too long string into password field")
        passw.send_keys(Keys.RETURN)
        print("Test action: Click ENTER button")
        assert "Грешни адрес или парола." in self.driver.page_source
        print("Test result: Login page is displayed and message: 'Грешни адрес или парола.'")
        
    def test_5_login_successful(self):
        self.driver = DRIVER
        user = self.driver.find_element_by_name("user")
        user.send_keys(userName)
        print("\nTest action: Set correct string: '" + userName + "' into username field")
        passw = self.driver.find_element_by_name("pass")
        passw.send_keys(password)
        print("Test action: Set correct string: ********** into password field")
        passw.send_keys(Keys.RETURN)
        print("Test action: Click ENTER button")
        elem = self.driver.find_element_by_xpath("//*[@id='continue-link']/h3")
        elem.click()
        assert "Ново писмо" in self.driver.page_source
        print("Test result: User is login. Profile home page is displayed.")
   
