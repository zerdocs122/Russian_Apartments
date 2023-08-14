from selenium import webdriver
import time
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pytest


options = webdriver.ChromeOptions()
options.set_capability('greneral.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

"""Опции направленные на обход CloudFlare"""
# options.add_argument('--headless') #Запкуск браузера в фоновом режиме, если потребуется

driver = webdriver.Chrome(r'C:\Users\Михаил\OneDrive\Рабочий стол', options=options) #Инициализация драйвера
    
stealth(driver=driver,
            languages=['ru', 'ru'],
            platform='win64',
            webgl_vendor='Intel Inc',
            renderer='Intel Iris OpenGL Engine',
            fix_hairline=True) # Делаем браузер похожим на реального человека с помощью оболочки stealth для Selenium
    
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source':
            '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
            '''
    }) # Удаляем методы у объекта window в браузере для обхода CloudFlare
    
""""Рекомендуется запускать тесты по отдельности ,так как при запуске всех тестов сразу, тесты запускаются в фоновом режиме, и не проходят проверку CloudFlare"""

def test_search():
    try:
        driver.get('https://ya.ru/') #переходим по заданному url 
        time.sleep(3) #Засыпаем на 3 секунды
        search = driver.find_element(By.XPATH, '//input[@class="search3__input mini-suggest__input"]') # Находим элемент на странице по параметру XPATH 
        time.sleep(3)
        assert search is not None #Проверяем есть ли элемент на странице
    except Exception as ex:
        print(ex) #Выводим ошибки если таковые имеются
    finally:         
        driver.close() #Закрываем вкладку
        driver.quit() #Закрываем браузер
        
def test_suggest():
    try:
        driver.get('https://ya.ru/')
        time.sleep(3)
        search = driver.find_element(By.XPATH, '//input[@class="search3__input mini-suggest__input"]')
        time.sleep(3)
        search.send_keys('Тензор')
        time.sleep(3)
        suggest = driver.find_element(By.XPATH, '//li[@class="mini-suggest__item mini-suggest__item_type_fulltext mini-suggest__item_personal_yes mini-suggest__item_with-button"]')
        time.sleep(3)
        assert suggest is not None
    except Exception as ex:
        print(ex)
    finally:         
        driver.close()
        driver.quit()
            
def test_block():
    try:
        driver.get('https://ya.ru/')
        time.sleep(3)
        search = driver.find_element(By.XPATH, '//input[@class="search3__input mini-suggest__input"]')
        time.sleep(3)
        search.send_keys('Тензор')
        time.sleep(3)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.XPATH, '//button[@class="Button2 DistrSplashscreen-DeclineButton"]').click()
        time.sleep(3)
        block = driver.find_element(By.XPATH, '//div[@class="main__center"]')
        time.sleep(3)
        assert block is not None
    except Exception as ex:
        print(ex)
    finally:         
        driver.close()
        driver.quit()

def test_link():
    try:
        driver.get('https://ya.ru/')
        time.sleep(3)
        search = driver.find_element(By.XPATH, '//input[@class="search3__input mini-suggest__input"]')
        time.sleep(3)
        search.send_keys('Тензор')
        time.sleep(3)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.XPATH, '//button[@class="Button2 DistrSplashscreen-DeclineButton"]').click()
        time.sleep(3)
        link = driver.find_element(By.LINK_TEXT, 'tensor.ru')
        time.sleep(3)
        assert link is not None
    except Exception as ex:
        print(ex)
    finally:         
        driver.close()
        driver.quit()    

   
    
       


















    