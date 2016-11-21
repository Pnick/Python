from selenium import webdriver
from commonPopupEntry import entryPassword

userName = "pnick@mail.bg"
password=entryPassword
global DRIVER
DRIVER = webdriver.Chrome("..\chromedriver_win32\chromedriver.exe")
DRIVER.get('http://www.mail.bg')

