#Price match between amazon and ebay grabbing the top 5 results in both
from operator import truediv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#op = webdriver.ChromeOptions()
#op.add_argument('headless')

op = Options()
op.headless = True
op.add_argument("--window-size=1920,1200")

#driver = webdriver.Chrome(options=op, service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Amazon search
driver.get('https://www.amazon.com')
searchbox = driver.find_element(By.ID, "twotabsearchtextbox")
searchbox.send_keys('ACP UPS 1500VA')
searchbox.submit()

time.sleep(2)

results = driver.find_elements(By.CSS_SELECTOR, ".s-result-item h2.a-size-mini") #gathers results from page
#prices = driver.find_elements(By.CSS_SELECTOR, ".s-result-item a.a-size-base")
prices = driver.find_elements(By.CLASS_NAME, "a-price")
f = open('results.txt', 'w')

#prints 5 results
x=0
amazon = 'Amazon Search Results'
print(amazon)
f.write(amazon)
f.write("\n")
for result in results:
    if x == 5:
        break
    print(result.text)
    f.write(result.text)
    f.write("\n")
    y=0
    for price in prices:
        if y == x:    
            print(price.text)
            f.write(price.text)
            f.write("\n")
            break
        elif y != x:
            y += 1
    x += 1

#Ebay search
driver.get("https://www.ebay.com")
searchbox = driver.find_element(By.ID, "gh-ac")
searchbox.send_keys('ACP UPS 1500VA')
searchbox.submit()

time.sleep(2)

results = driver.find_elements(By.CLASS_NAME, "s-item__title") #gathers results from page
prices = driver.find_elements(By.CLASS_NAME, "s-item__price")

#prints 5 results
x=0
ebay = "Ebay Search Results"
for result in results:
    if x == 5:
        break
    elif x == 0:
        print(ebay)
        f.write(ebay)
        f.write("\n")
    else:
        y=0
        print(result.text)
        f.write(result.text)
        f.write("\n")
        for price in prices:
            if y == x:    
                print(price.text)
                f.write(price.text)
                f.write("\n")
                break
            elif y != x:
                y += 1
    x += 1

f.close()

driver.quit()