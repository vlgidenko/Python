import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.amazon.com')
searchbox = driver.find_element(By.ID, "twotabsearchtextbox")
searchbox.send_keys('potato')
searchbox.submit()

time.sleep(2)

results = driver.find_elements(By.CSS_SELECTOR, ".s-result-item h2.a-size-mini") #gathers results from page

#prints all results
for result in results:
    print(result.text)

driver.quit()