import pytest
import time
import allure
from selenium import webdriver
import selenium.webdriver.chrome.options
from selenium.webdriver.common.be import By
from selenium.webdriver.common.alert import alert

@pytest.fixture(scope='class')
def setup(request):
    chrome_options=Options()
    driver = webdriver.Chromr(options=chrome_options)
    driver.implicitly_wait(10)
    driver.set_window_size(1920,1080)
    request.cls.driver = driver
    yield driver
    driver.close()
