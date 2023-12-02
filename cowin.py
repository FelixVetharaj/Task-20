#Task -20 -https://www.cowin.gov.in/

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Cowin:

    #Constructor parameter
    def __init__(self, url):
        self.url = url
         #Install latest web driver manager
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def login(self):
        self.driver.get(url)
        sleep(2)
        self.driver.find_element(By.XPATH, '//a[@href="/faq" and @class="dropdwnbtn accessibility-plugin-ac newMenu"]').click()
        sleep(2)
        print(self.driver.title)
        print(self.driver.current_url)
        self.driver.find_element(By.XPATH, '//a[@href="/our-partner"]').click()
        sleep(5)
        print(self.driver.title)
        print(self.driver.current_url)
        print(self.driver.current_window_handle) # 96f1f7cb-2f5d-4b2e-b171-736ec076841b- Parent handle
        handles = self.driver.window_handles
        print(handles)

        for handle in handles:
            self.driver.switch_to.window(handle)
            print(self.driver.current_url)
            print(self.driver.title)
            if self.driver.current_url == 'https://www.cowin.gov.in/our-partner':
                 self.driver.close()
            elif self.driver.current_url == 'https://www.cowin.gov.in/faq':
                 self.driver.close() 
                  

url = "https://www.cowin.gov.in/"
c = Cowin(url)
c.login()

