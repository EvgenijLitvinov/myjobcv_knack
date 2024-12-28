from conf import *
import keyboard
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome()

driver.get('https://myjobcv.knack.com/app2#-/')
keyboard.wait('esc')
