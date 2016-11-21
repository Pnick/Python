from unittest import TestCase
from commonWebDriver import DRIVER

class ClosePageTest(TestCase):
    
    def test_6_close_page(self):
        self.driver = DRIVER
        elem = DRIVER.find_element_by_xpath("//*[@id='right_navigation']/li[1]/a")
        elem.click()
        print("\nTest action: Click CLOSE button")
        assert "Имейл адрес:" or "Вие заключихте пощенската си кутия."  in self.driver.page_source
        print("Test result: Successful Exit from profile page")
        #self.driver.quit()
