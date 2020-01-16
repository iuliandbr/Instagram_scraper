from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep

cwd = os.getcwd()
firefox_path = cwd + r'\geckodriver.exe'
webdriver = webdriver.Firefox(executable_path=firefox_path)
sleep(1)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('iuliandbr')
password = webdriver.find_element_by_name('password')
password.send_keys('Di11081992')

button_login = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
button_login.click()
sleep(3)

