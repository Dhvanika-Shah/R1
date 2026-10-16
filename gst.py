import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
get_site = "https://services.gst.gov.in"
# Let's make a driver to start the application
driver = webdriver.Chrome(options=chrome_options) # service=service,
# Open the website
driver.get(get_site)
time.sleep(15)
