from selenium import webdriver
from time import sleep
a = 1
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input("Enter the Friend's Name OR Group Name : ")
   
msg = input('Enter your message : ')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msgBox = driver.find_element_by_class_name("box class name")
while(True):
   sleep(1)
   print(a)
   a += 1
   msgBox.send_keys(msg)
   button = driver.find_element_by_class_name('button class name')
   button.click()
