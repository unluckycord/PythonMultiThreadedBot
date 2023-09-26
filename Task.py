# Define a function that prints numbers from 1 to 10

from selenium import webdriver
from selenium.webdriver.common.by import By


# Using Chrome to access web
#driver = webdriver.Chrome()
#driver.get("https://www.selenium.dev/selenium/web/web-form.html")


def init():
    driver = webdriver.Chrome()
    Access_Accounts(driver)
    Action_Carried_Out(driver)


def Access_Accounts(driver):
    driver.get("https://www.instagram.com")
    #print(driver.page_source)
    driver.implicitly_wait(20)
    username = driver.find_element(by=By.NAME, value = "username")
    username.clear
    username.send_keys('username')
    password = driver.find_element(by=By.NAME, value = "password")
    password.clear
    password.send_keys('password')
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '/html/body')

def Action_Carried_Out(driver):
    driver.find_element(By.XPATH, '//*[@id="mount_0_0_VR"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div/svg/path').click()
    #driver.find_element(By.NAME, "Log in").click()