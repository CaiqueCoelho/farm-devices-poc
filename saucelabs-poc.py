from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import os

caps = {}
caps['platformName'] = 'Android'
caps['browserName'] = 'Chrome'
caps['appium:deviceName'] = 'Google Pixel 4a (5G) GoogleAPI Emulator'
caps['appium:platformVersion'] = '12.0'
caps['sauce:options'] = {}
caps['sauce:options']['appiumVersion'] = '1.22.1'

url = os.environ.get('SAUCELABS_URL')
driver = webdriver.Remote(url, caps)