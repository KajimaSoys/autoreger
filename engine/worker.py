from selenium import webdriver
import time

from selenium.webdriver.common import actions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import dataloader


def driverwork(driver):
    # достаем инфу из документов и рандомим случайные выражения
    gender = bool(random.getrandbits(1))
    name, surname = dataloader.dataload(gender)

    # Отправляем имя из бд
    nameform = driver.find_element_by_xpath('//*[@id="fname"]')
    nameform.click()
    nameform.send_keys(name)

    # Отправляем фамилию из бд
    surform = driver.find_element_by_xpath('//*[@id="lname"]')
    surform.click()
    surform.send_keys(surname)

    # Устанавливаем день
    item = driver.find_element_by_css_selector(':nth-child(5) > :nth-child(2) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1)')
    item.click()
    day = '#react-select-2-option-' + str(random.randint(0, 28)) + ' > :nth-child(1) > :nth-child(1)'
    option = driver.find_element_by_css_selector(day)
    option.click()

    # Месяц
    item = driver.find_element_by_css_selector(':nth-child(2) > :nth-child(1) > :nth-child(3) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1)')
    item.click()
    month = '#react-select-3-option-' + str(random.randint(0, 11)) + ' > :nth-child(1) > :nth-child(1)'
    option = driver.find_element_by_css_selector(month)
    option.click()

    # Год
    item = driver.find_element_by_css_selector(':nth-child(5) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1)')
    item.click()
    year = random.randint(20, 60)
    yearsel = '#react-select-4-option-' + str(year) + ' > :nth-child(1) > :nth-child(1)'
    option = driver.find_element_by_css_selector(yearsel)
    option.click()

    # Пол
    if gender:
        gender = driver.find_element_by_xpath("//label[div[input[@value='male']]]").click()
        # gender.find_element_by_class_name('border-0-2-97').click()
        # actions.moveToElement(driver.findElement(By.XPATH("//input[@value='male']"))).click().perform();
    else:
        gender = driver.find_element_by_xpath("//label[div[input[@value='female']]]").click()
        # gender.find_element_by_class_name('border-0-2-97').click()
        # actions.moveToElement(driver.findElement(By.XPATH("//input[@value='female']"))).click().perform();

    # Имя аккаунта
    login = usernameform(driver, year)

    # Пароль
    passbutton = driver.find_element_by_xpath('//a[@data-test-id="generate-password"]')
    passbutton.click()
    passform = driver.find_element_by_xpath('//input[@name="password"]')
    password = passform.get_attribute('value')
    print('Старина, не забудь от цифр избавиться во времся формирования юзернейма')
    print(login, password)


    return login, password


def usernameform(driver, year):
    logform = driver.find_element_by_xpath('//*[@id="aaa__input"]')
    logform.click()
    time.sleep(3)
    var = '//div[@data-test-id="alternative-email-' + str(random.randint(0, 7)) + '"]'
    temp = driver.find_element_by_xpath(var)
    username = temp.get_attribute('data-email')

    sep = '@'
    rest = username.split(sep, 1)[0]
    dot = '.'
    year = str(2021 - year)[2:]
    username = dot.join([rest, year])
    print(username)
    login = username + '@mail.ru'

    logform = driver.find_element_by_xpath('//*[@id="aaa__input"]')
    logform.click()
    logform.send_keys(username)

    return login
