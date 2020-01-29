from selenium import webdriver
from time import sleep
a = 1
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input("Enter the name: ")
   
fileToSend = "/home/muneeb/Desktop/TREE.JPG"
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
driver.find_element_by_css_selector('span[data-icon="clip"]').click()
# add file to send by file path
attach=driver.find_element_by_css_selector('input[type="file"]')
# click to add
attach.send_keys(fileToSend)
sleep(5)
button=driver.find_element_by_xpath("//div[contains(@class, 'class name')]")
button.click()
