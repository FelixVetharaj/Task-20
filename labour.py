#Task -20 -https://labour.gov.in/

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class Labour:

    def __init__(self, url):
        self.url = url
        options = webdriver.FirefoxOptions()
        
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def documents(self): 
        try:

            self.driver.maximize_window()
            self.driver.get(self.url)              
            elementToHover = self.driver.find_element(By.XPATH, '//a[text()="Documents"]')
            hover = ActionChains(self.driver).move_to_element(elementToHover)
            hover.perform()               
            sleep(2)
            self.driver.find_element(By.XPATH, '//a[@href="https://labour.gov.in/monthly-progress-report"]').click()
            sleep(4)
            self.driver.find_element(By.XPATH, '//a[@href="https://labour.gov.in/sites/default/files/mpr_sept_2023.pdf"]').click()
            sleep(5)
            alert = self.driver.switch_to.alert
            alert.accept()
            sleep(5)

            print(self.driver.current_window_handle)
            handles = self.driver.window_handles
            print(handles)

            for handle in handles:
                self.driver.switch_to.window(handle)
                print(self.driver.current_url)
            
                if self.driver.current_url == "https://labour.gov.in/monthly-progress-report":
                    print(self.driver.current_url)
                    print(self.driver.title)

                elif self.driver.current_url == "https://labour.gov.in/sites/default/files/mpr_sept_2023.pdf":
                    print(self.driver.current_url)
                    print(self.driver.title)
                    self.driver.find_element(By.ID, "download").click()
        except NoSuchElementException as error:
            print(error)
        finally:
            self.driver.quit()

    def media(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            elementToHover = self.driver.find_element(By.XPATH, '//a[text()="Media"]')
            ActionChains(self.driver).move_to_element(elementToHover).perform()
            self.driver.find_element(By.XPATH, '//a[text()="Photo Gallery"]').click()
            sleep(5)
            hover = self.driver.find_element(By.XPATH, '//img[@title="Swachhata Hi Seva"]')
            ActionChains(self.driver).move_to_element(hover).context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()
            sleep(10)
            
        except NoSuchElementException as error:
            print(error)
        finally:
            self.driver.quit()
                    

url = "https://labour.gov.in/"
l = Labour(url)
#l.documents()
l.media()
