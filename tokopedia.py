import time
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec

nope = ('087830348614')
driver = webdriver.Chrome()
driver.get('https://www.tokopedia.com')

try:
    daftar = driver.find_element(By.XPATH,'//*[@id="header-main-wrapper"]/div[2]/div[5]/button[2]')
    daftar.click()
except:
    print('Sudah Otomatis')

insert_nope = driver.find_element(By.XPATH, '//*[@id="regis-input"]')
insert_nope.send_keys(nope)
driver.find_element(By.XPATH, '//*[@id="zeus-root"]/div/main/div[2]/div[2]/div/div[2]/form/button').click()
confirmasi = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[2]/button[1]'))
)
try:
    confirmasi.click()
except:
    confirm_wa = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="zeus-root"]/div/div[2]/section/div/div/div[2]/div'))
    )
    confirm_wa.click()
time.sleep(10)
