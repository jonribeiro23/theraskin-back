from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
from pprint import pprint

chrome_options = Options()
chrome_options.add_argument('--headless')

chrome_path = which('chromedriver')

driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
driver.get('https://www.epocacosmeticos.com.br/serum-anti-idade-theraskin-euryale-qr/p')

search_input = driver.find_elements_by_xpath("//div[@class='ts-review']")
print()
for box in search_input:
    print('')
    print(box.text)

driver.close()
