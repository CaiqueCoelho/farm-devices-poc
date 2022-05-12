from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
  
desired_cap = {
    # Set your access credentials
    "browserstack.user" : os.environ.get('BROWSERSTACK_USER'),
    "browserstack.key" : os.environ.get('BROSERSTACK_KEY'),
  
    # Set URL of the application under test
    "app" : os.environ.get('BROSERSTACK_APP_URL'),
  
    # Specify device and os_version for testing
    "device" : "Google Pixel 3",
    "os_version" : "9.0",
      
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-1",
    "name" : "first_test"
}
  
# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)
  
# If you have uploaded your app, write your test case here. 
search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "caiquecoelho.com.testeeneagrama:id/login_button_invited"))
)
search_element.click()
  
# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()