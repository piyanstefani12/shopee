import time
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec

def Shopee(nope):
    driver = webdriver.Chrome()
    driver.get('https://www.shopee.co.id')

    try:
        login = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/header/div[1]/nav/ul/a[3]')))
    except selenium.common.exceptions.TimeoutException:
        print('Sudah Otomatis')

    nope_click = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/a[2]'))
    )
    nope_click.click()
    send_nope = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[1]/input'))

    )
    send_nope.send_keys(nope)
    berikutnya = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button'))
    )
    berikutnya.click()
    captcha = input("Selesaikan Captcha: (Tekan Y Jika Sudah: ")
    if captcha == 'Y':
        pass
    else:
        captcha

    kirim = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="modal"]/aside/div[1]/div/div[2]/button[3]'))
    )

    kirim.click()
    driver.close()