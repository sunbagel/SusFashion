import os
from selenium import webdriver


os.environ['PATH'] += r"./chromedriver_win32"
driver = webdriver.Chrome()