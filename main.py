from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import config
import datetime


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
    l = ["подходящих вакансий","подходящие вакансии","подходящяя вакансия"]
    if button.get_attribute("innerHTML").split(';')[-1].split("<!-- -->")[-1].split("</a>")[0] in l:
        print("wait")
    else:
        button.click()
    driver.close()
    return Time()

def Time()->str:
    '''Returns time to make a task for task manager'''
    return str(datetime.datetime.now()).split(' ')[-1]


Login()
