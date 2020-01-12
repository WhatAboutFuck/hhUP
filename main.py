from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import config 



def Login():
    options = Options()
    options.add_argument(("user-agent={}").format(config.headers))
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get(config.link)
    driver.find_element_by_name("username").send_keys(config.login)
    driver.find_element_by_name("password").send_keys(config.password)
    driver.find_element_by_xpath((".//input[@value='Войти в личный кабинет']")).click()
    driver.implicitly_wait(4)
    button = driver.find_element_by_class_name("applicant-resumes-recommendations-button")
    if button.get_attribute("innerHTML").split(';')[-1].split("<!-- -->")[-1].split("</a>")[0] == "подходящие вакансии":
        print("wait")
    else:
        button.click()
    x = driver.find_element_by_class_name("applicant-resumes-update").get_attribute("innerHTML")
    driver.close()
    return x

def Time(s=Login())->str:
    '''Returns time to make a task for task manager'''
    return s.split(";")[-1].split("<")[0]

Time()
