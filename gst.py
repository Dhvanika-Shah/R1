import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
get_site = "https://services.gst.gov.in"
# We set the driver Path
#chromedriver_path='c:\dhvanika\Python\seleniumDriver\chromeSpecial.exe'
# We set the special chrome for working
#chrome_options.binary_location="c:\dhvanika\Python\seleniumDriver\chrome\chrome.exe"
# Let's make a driver to start the application
driver = webdriver.Chrome(options=chrome_options) # service=service,
# Open the website
driver.get(get_site)
time.sleep(15)
a=driver.find_element(By.XPATH,"/html/body/div[1]/ng-include/nav/div/div/ul/li[2]/a").click()
un="abc"
pw="abc"
txtun=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div/div/input")
time.sleep(2)
txtun.send_keys(un)
txtpw=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/form/div[3]/div/div/input")
time.sleep(2)
txtpw.send_keys(pw)
time.sleep(15)
