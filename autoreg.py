from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import time

options = webdriver.ChromeOptions() 
options.add_argument("download.default_directory=D:\Учеба\АИС\torgi_parser_Efim")
driver = webdriver.Chrome(options=options,executable_path=r'C:\Users\Kajima\chromedriver.exe')# путь к драйверу chrome

driver.get('https://account.mail.ru/signup?from=main&rf=auth.mail.ru')
#кусок ниже не трогался
download_button = driver.find_element_by_id('id19')
download_button.click()
wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="_wicket_window_0"]')))

driver.find_element_by_xpath('/html/body')
driver.find_element_by_xpath('//*[@id="_wicket_window_1"]')

select = Select(driver.find_element_by_xpath('//*[@id="id23"]'))
select.select_by_value('5')
    
download_button = driver.find_element_by_xpath('//*[@id="id27"]')
download_button.click()

time.sleep(20)
driver.quit()
