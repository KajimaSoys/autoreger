from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import time
import random

#достаем инфу из документов и рандомим случайные выражения
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

day=random.randint(0,5)


#подключаем вебдрайвер
options = webdriver.ChromeOptions() 
options.add_argument("download.default_directory=D:\Учеба\АИС\torgi_parser_Efim")
driver = webdriver.Chrome(options=options,executable_path=r'C:\Users\Kajima\chromedriver.exe')# путь к драйверу chrome
#страница регистрации
driver.get('https://account.mail.ru/signup?from=main&rf=auth.mail.ru')

nameform = driver.find_element_by_xpath('//*[@id="fname"]')
nameform.click()
nameform.send_keys(namedb[nameindex])

surform = driver.find_element_by_xpath('//*[@id="lname"]')
surform.click()
surform.send_keys(surdb[surindex])
time.sleep(3)
dselect = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/form/div[5]/div[2]/div/div[1]/div/div')
dselect.click()
#dselect = Select(driver.find_element_by_class_name('select-0-2-241'))                                               
#dselect.select_by_value('3')
time.sleep(10)
dselect = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/form/div[5]/div[2]/div/div[1]/div/div')
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/form/div[5]/div[2]/div/div[1]/div/div').send_keys(Keys.DOWN)
driver.send_keys(Keys.DOWN).perform()
#dselect.click()

#for i in range(day):
#    dselect.send_keys(Keys.ARROW_DOWN).perform()
#    time.sleep(1)
#dselect.send_keys(Keys.RETURN)

time.sleep(200)
driver.quit()
