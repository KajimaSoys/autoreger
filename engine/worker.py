from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import datawork
import captchatemp

def driverwork(driver):
    time.sleep(3)
    # достаем инфу из документов и рандомим случайные выражения
    gender = bool(random.getrandbits(1))
    name, surname = datawork.dataload(gender)
    login = 'tipa'
    password = 'ok'
    sendname(driver, name)
    sendsurname(driver, surname)
    year = birthday(driver)
    sendgender(driver, gender)
    login = usernameform(driver, year)
    password = formpassword(driver)
    # time.sleep(3)
    sendbutton(driver)
    time.sleep(5)
    captcha = captchasolver(driver)
    sendcaptcha(driver, captcha)
    print(login, password)
    return login, password

    # Отправляем имя из бд


def sendcaptcha(driver, captcha):
    captchaform = driver.find_element_by_xpath('//*[@data-test-id="captcha"]')
    captchaform.click()
    captchaform.send_keys(captcha)
    sendbutton1 = driver.find_element_by_xpath('//*[@data-test-id="verification-next-button"]')
    sendbutton1.click()


def sendname(driver, name):
    nameform = driver.find_element_by_xpath('//*[@id="fname"]')
    nameform.click()
    nameform.send_keys(name)

    # Отправляем фамилию из бд


def sendsurname(driver, surname):
    surform = driver.find_element_by_xpath('//*[@id="lname"]')
    surform.click()
    surform.send_keys(surname)

    # Дата рождения


def birthday(driver):
    # Устанавливаем день
    item = driver.find_element_by_css_selector(
        ':nth-child(5) > :nth-child(2) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1)')
    item.click()
    day = '#react-select-2-option-' + str(random.randint(0, 28)) + ' > :nth-child(1) > :nth-child(1)'
    option = driver.find_element_by_css_selector(day)
    option.click()

    # Месяц
    item = driver.find_element_by_css_selector(
        ':nth-child(2) > :nth-child(1) > :nth-child(3) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1)')
    item.click()
    month = '#react-select-3-option-' + str(random.randint(0, 11)) + ' > :nth-child(1) > :nth-child(1)'
    option = driver.find_element_by_css_selector(month)
    option.click()

    # Год
    item = driver.find_element_by_css_selector(
        ':nth-child(5) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1) > :nth-child(1)')
    item.click()
    year = random.randint(20, 60)
    yearsel = '#react-select-4-option-' + str(year) + ' > :nth-child(1) > :nth-child(1)'
    option = driver.find_element_by_css_selector(yearsel)
    option.click()
    return year

    # Пол


def sendgender(driver, gender):
    if gender:
        gender = driver.find_element_by_xpath("//label[div[input[@value='male']]]").click()
        # gender.find_element_by_class_name('border-0-2-97').click()
        # actions.moveToElement(driver.findElement(By.XPATH("//input[@value='male']"))).click().perform();
    else:
        gender = driver.find_element_by_xpath("//label[div[input[@value='female']]]").click()
        # gender.find_element_by_class_name('border-0-2-97').click()
        # actions.moveToElement(driver.findElement(By.XPATH("//input[@value='female']"))).click().perform();

    # Пароль


def formpassword(driver):
    passbutton = driver.find_element_by_xpath('//a[@data-test-id="generate-password"]')
    passbutton.click()
    passform = driver.find_element_by_xpath('//input[@name="password"]')
    password = passform.get_attribute('value')
    return password

    # Кнопка отправить


def sendbutton(driver):
    button = driver.find_element_by_css_selector(
        'body > div.page-content > div:nth-child(3) > div.App-mobile__wrapper---iGyl > div > div > div > div > form > button')
    button.click()
    # driver.implicitly_wait(10)
    # ActionChains(driver).move_to_element(button).click(button).perform()

def captchasolver(driver):
    with open('test.png', 'wb') as file:
        file.write(driver.find_element_by_class_name(
            'styles-mobile__captchaImage--sHzh3').screenshot_as_png)
    captcha = captchatemp.run()
    return captcha


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
    rest = ''.join([i for i in rest if not i.isdigit()])
    year = str(2021 - year)[2:]
    username = dot.join([rest, year])
    username = username.replace('..', '.')
    print(username)
    login = username + '@mail.ru'

    logform = driver.find_element_by_xpath('//*[@id="aaa__input"]')
    logform.click()
    logform.send_keys(username)

    return login
