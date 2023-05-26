from time import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

roll_no="YOUR ROLL NO"
passwd="YOUR PASSWORD"

service = Service(executable_path="C://Users//ajeet//OneDrive//Desktop//NetAccess//ChromeDriver//chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://netaccess.iitm.ac.in/account/login")

"""
advanced=driver.find_element(By.ID,"details-button")
advanced.click()



unsafebut=driver.find_element(By.ID,"proceed-link")
unsafebut.click()
"""


elem=driver.find_element(By.NAME,'userLogin')
elem.clear()
elem.send_keys(roll_no)



password=driver.find_element(By.NAME,'userPassword')
password.clear()
password.send_keys(passwd)



submit=driver.find_element(By.NAME,'submit')
submit.click()



driver.find_element(By.LINK_TEXT,"approve").click()


but=driver.find_element(By.ID,"radios-1").click()


auth=driver.find_element(By.NAME,"approveBtn").click()


driver.close()


