from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import worker
import proxy

def main():

  options = {
    'proxy':
      {
        'http': 'http://lum-customer-hl_79a92981-zone-static-country-ru:f9ad1zb48xxp@zproxy.lum-superproxy.io:22225',
        'https': 'https://lum-customer-hl_79a92981-zone-static-country-ru:f9ad1zb48xxp@zproxy.lum-superproxy.io:22225'
      },
  }
  PATH = 'C:\Program Files (x86)\Python38-32/chromedriver.exe'
  driver = webdriver.Chrome(PATH,seleniumwire_options=options)

  #тест, что айпи меняется
  #driver.get("https://lumtest.com/myip.json")
  #print(driver.execute_script('return document.body.innerHTML;'))  # print page html
  #time.sleep(3)

  # страница регистрации
  #driver.get('https://2ip.ru')
  driver.get('https://account.mail.ru/signup?from=vk')
  try:
    login,password = worker.driverwork(driver)
    pass
  except Exception as e:
    print(e)
  finally:
    time.sleep(30)
    driver.quit()


if __name__ == "__main__":
  main()







