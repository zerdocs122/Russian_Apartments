from selenium import webdriver
import time
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pytest
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.set_capability('greneral.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument('--headless')
driver = webdriver.Chrome(r'C:\Users\Михаил\OneDrive\Рабочий стол', options=options)

    
stealth(driver=driver,
            languages=['ru', 'ru'],
            platform='win64',
            webgl_vendor='Intel Inc',
            renderer='Intel Iris OpenGL Engine',
            fix_hairline=True)
    
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source':
            '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
            '''
    })

try:
    driver.get('https://ya.ru/')
    time.sleep(3)
    search = driver.find_element(By.XPATH, '//input[@class="search3__input mini-suggest__input"]').click()
    services = driver.find_element(By.XPATH, '//a[@class="home-link2 services-suggest__item services-suggest__item-more home-link2_color_black home-link2_hover_secondary"]').click()
    time.sleep(1)
    image = driver.find_element(By.XPATH, '//a[@aria-label="Картинки"]').click()
    time.sleep(1)
    driver.get('https://ya.ru/images/search?text=%D0%9F%D1%82%D0%B8%D1%86%D0%B0%20%D0%A1%D0%B5%D0%BA%D1%80%D0%B5%D1%82%D0%B0%D1%80%D1%8C&amp;nl=1&amp;source=morda')
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    img_link = driver.find_elements(By.XPATH, '//a[@class="serp-item__link"]')
    print(img_link)
    time.sleep(1)
    img_link[0].click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//div[@class="MMThumbImage MMThumbImage_fit_square ImagesViewerGallery-Thumb"]').click()
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:         
    driver.close()
    driver.quit()