from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get('https:login.salesforce.com')
driver.maximize_window()
