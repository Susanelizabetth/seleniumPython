from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait

from contextlib import contextmanager


@contextmanager
def wait_for_new_window(driver, timeout=10):
    handles_before = driver.window_handles
    yield
    WebDriverWait(driver, timeout).until(
        lambda driver: len(handles_before) != len(driver.window_handles))


driver = webdriver.Chrome('C:/chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get('https://www.amazon.com/')

# Search for a product HP Pavilion azul
keyword = "HP Pavilion azul"
# create WebElement for a search box
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
# type the keyword in searchbox
search_box.send_keys(keyword)
# create WebElement for a search button
driver.find_element(By.ID, 'nav-search-submit-button').click()

driver.find_element(
    By.CSS_SELECTOR, '.a-link-normal').click()

driver.find_element(By.ID, 'quantity').send_keys(2)
driver.find_element(By.ID, 'add-to-cart-button').click()
driver.find_element(By.ID, 'sw-gtc').click()
# wait for the page to download
with wait_for_new_window(driver, 2):
    pass
# quit the driver after finishing scraping (please keep this line at the bottom)
driver.quit()
# time.sleep(5000)
