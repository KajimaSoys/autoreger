from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import time
import random

fmn = open('res/male_name.txt',encoding='utf-8')
fs = open('res/surnames.txt',encoding='utf-8')
namedb=[]
surdb=[]
for line in fmn:
    line=line.replace('\n','')
    namedb.append(line)
for line in fs:
    line=line.replace('\n','')
    surdb.append(line)
nameindex=random.randint(0,len(namedb))
surindex=random.randint(0,len(surdb))
print(surdb[surindex]+' '+namedb[nameindex])
fmn.close()
fs.close()

options = webdriver.ChromeOptions() 
options.add_argument("download.default_directory=D:\Учеба\АИС\torgi_parser_Efim")
driver = webdriver.Chrome(options=options,executable_path=r'C:\Users\Kajima\chromedriver.exe')# путь к драйверу chrome

driver.get('https://account.mail.ru/signup?from=main&rf=auth.mail.ru')
#кусок ниже не трогался
nameform = driver.find_element_by_xpath('//*[@id="fname"]')
nameform.click()
nameform.send_keys(namedb[nameindex])

surform = driver.find_element_by_xpath('//*[@id="lname"]')
surform.click()
surform.send_keys(surdb[surindex])


time.sleep(200)
driver.quit()
