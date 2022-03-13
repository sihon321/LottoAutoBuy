import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def main():
    driver = set_chrome_driver()

    driver.get('https://dhlottery.co.kr/common.do?method=main')

    handle_popup_window(driver)

    login(driver)

    time.sleep(2)

    handle_popup_window(driver)
    time.sleep(2)
    click_lotto(driver)

    buy_auto_lotto(driver)

def buy_auto_lotto(driver):
    driver.implicitly_wait(2)
    windows_list = driver.window_handles
    windows_list_count = len(windows_list)
    driver.switch_to.window(windows_list[windows_list_count-1])
    driver.switch_to.frame('ifrm_tab')

    driver.find_element(By.XPATH, '//*[@id="num2"]').click()
    driver.find_element_by_xpath('//*[@id="btnSelectNum"]').click()
    driver.find_element_by_xpath('//*[@id="btnBuy"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="popupLayerConfirm"]/div/div[2]/input[1]').click()
    time.sleep(2)

def click_lotto(driver):
    driver.find_element_by_xpath('//*[@id="gnb"]/ul/li[1]/a').click()
    driver.find_element_by_xpath('//*[@id="gnb"]/ul/li[1]/div/ul/li[1]/a').click()

def login(driver):
    driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/form/div/ul/li[1]/a').click()
    driver.find_element_by_xpath('/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/input[1]')\
        .send_keys('')
    driver.find_element_by_xpath('//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/input[2]')\
        .send_keys('')
    driver.find_element_by_xpath('//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a').click()

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def handle_popup_window(driver):
    windows_list = driver.window_handles
    windows_list_count = len(windows_list)
    count = 1
    print(windows_list_count)
    while count < windows_list_count:
        driver.switch_to.window(windows_list[count])
        driver.close()
        count += 1
    driver.switch_to.window(windows_list[0])


main()