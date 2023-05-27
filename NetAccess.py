# Importing Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Roll Number and Password
roll_no="YOUR ROLL NO"
passwd="YOUR PASSWORD"

service = Service(executable_path="PATH TO CHROME DRIVER")
driver = webdriver.Chrome(service=service)

driver.get("http://netaccess.iitm.ac.in/account/login")

"""
advanced=driver.find_element(By.ID,"details-button")
advanced.click()



unsafebut=driver.find_element(By.ID,"proceed-link")
unsafebut.click()
"""

# Fill in the Username Field
elem=driver.find_element(By.NAME,'userLogin')
elem.clear()
elem.send_keys(roll_no)

#Fill in the Password Field
password=driver.find_element(By.NAME,'userPassword')
password.clear()
password.send_keys(passwd)

#Press Buttons:
submit=driver.find_element(By.NAME,'submit')
submit.click()

driver.find_element(By.LINK_TEXT,"approve").click()

but=driver.find_element(By.ID,"radios-1").click()

auth=driver.find_element(By.NAME,"approveBtn").click()

#Close the webdriver instance
driver.close()


