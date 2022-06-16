# By: Eduardo Corazon
#Date: 5/31/2022
#Description: This is a
#

#!/usr/bin/python

# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

url = 'https://www.google.com/'

driver.get(url)

driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('This is a test to see speed')

# driver.find_element_by_xpath('').send_keys('')
