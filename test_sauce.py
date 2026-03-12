import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():  
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # driver.quit()
    

def test_sauce(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(3)
    
    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    print("Added bag")
    time.sleep(3)
    
    driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
    print("Added bike light")
    time.sleep(3)
    
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    time.sleep(3)
    
    
    driver.find_element(By.ID,"checkout").click()
    
    time.sleep(3)
    driver.find_element(By.ID,"first-name").send_keys("Sarathi")
    driver.find_element(By.ID,"last-name").send_keys("T")
    driver.find_element(By.ID,"postal-code").send_keys("605775")
    driver.find_element(By.ID,"continue").click()
    
    time.sleep(3)
    
    driver.find_element(By.ID,"finish").click()
    
    
    success=driver.find_element(By.CLASS_NAME,"complete-header").text


    assert "Thank you for your order!" in success
    
    driver.find_element(By.ID,"react-burger-menu-btn").click()
    
    time.sleep(3)
    
    driver.find_element(By.ID,"logout_sidebar_link").click()
    
    
    time.sleep(3)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    