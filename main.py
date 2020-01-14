from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import config1



def Login():
    options = Options()
    options.add_argument(("user-agent={}").format(config1.headers))
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    
    driver.get(config1.link)
    driver.find_element_by_name("username").send_keys(config1.login)
    driver.find_element_by_name("password").send_keys(config1.password)
    driver.find_element_by_xpath((".//input[@value='Войти в личный кабинет']")).click()
    driver.implicitly_wait(4)
    driver.find_element_by_xpath((".//button[@class='bloko-link bloko-link_dimmed']")).click()
    driver.close()
    return "Done!"



Login()
