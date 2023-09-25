# Define a function that prints numbers from 1 to 10

from selenium import webdriver
from selenium.webdriver.common.by import By


# Using Chrome to access web
#driver = webdriver.Chrome()
#driver.get("https://www.selenium.dev/selenium/web/web-form.html")


def Access_Accounts():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com")
    driver.implicitly_wait(20)
    username = driver.find_element(by=By.NAME, value = "username")
    username.clear
    username.send_keys("testemail@gmail.com")
    password = driver.find_element(by=By.NAME, value = "password")
    password.clear
    password.send_keys("password")
