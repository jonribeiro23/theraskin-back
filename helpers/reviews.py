from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from shutil import which
import os

class Reviews:
    def __init__(self) -> None:
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--deisable-dev-sh-usage')
        # chrome_path = which('chromedriver')
        # self.driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
        self.driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
    
    
    def get_review(self, url: str) -> list:
        self.driver.get(url)
        search_input = self.driver.find_elements_by_xpath("//div[@class='ts-review']")
        reviews = []
        for box in search_input:
            reviews.append({'comment': box.text})
        self.driver.close()
        return reviews