from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import worker


def main():
  # подключаем вебдрайвер
  options = webdriver.ChromeOptions()
  options.add_argument("download.default_directory=D:\Учеба\АИС\torgi_parser_Efim")
  driver = webdriver.Chrome(options=options)  # путь к драйверу chrome
  # страница регистрации
  driver.get('https://account.mail.ru/signup?from=vk')
  try:
    login,password = worker.driverwork(driver)
  except Exception as e:
    print(e)
  finally:
    time.sleep(30)
    driver.quit()


if __name__ == "__main__":
  main()







