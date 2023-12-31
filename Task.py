# Define a function that prints numbers from 1 to 10
import UsernameGen, PasswordGen

from selenium import webdriver
from selenium.webdriver.common.by import By
from PasswordGen import PasswordGenerator


# Using Chrome to access web
#driver = webdriver.Chrome()
#driver.get("https://www.selenium.dev/selenium/web/web-form.html")


def init():
    driver = webdriver.Firefox()
    website = "https://www.instagram.com"
    driver.get(website)
    
    UsernameGen.LoadNames()

    if(website == "https://www.instagram.com"):
        Instagram_Account_Access(driver)
        Action_Carried_Out(driver)

def Create_Instagram_Account():
    pass

def Instagram_Account_Access(driver):
    #print(driver.page_source)
    driver.implicitly_wait(20)
    username = driver.find_element(by=By.NAME, value = "username")
    username.clear
    username.send_keys(UsernameGen.UsernameGenerator())
    password = driver.find_element(by=By.NAME, value = "password")
    password.clear
    password.send_keys(str(PasswordGenerator))
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
    driver.implicitly_wait(60)

    #save login info button
    driver.find_element(By.XPATH, '//*[@id="mount_0_0_rO"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
    
    #enable notifications button
    driver.find_element(By.XPATH, '/html/body')

def Action_Carried_Out(driver):
    #search button
    driver.find_element(By.XPATH, '//*[@id="mount_0_0_VR"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div/svg/path').click()
    #driver.find_element(By.NAME, "Log in").click()