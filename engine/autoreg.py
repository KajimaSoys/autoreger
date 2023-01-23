import time
import worker
import proxy
import proxytest
import datawork

def main():
    driver = proxy.ON(False)
    #driver = proxytest.proxytake()

    # тест, что айпи меняется
    # driver.get("https://lumtest.com/myip.json")
    # print(driver.execute_script('return document.body.innerHTML;'))  # print page html
    # time.sleep(3)

    # страница регистрации
    #driver.get('https://2ip.ru')

    driver.get('https://account.mail.ru/signup?from=vk')

    try:
        login, password = worker.driverwork(driver)
        datawork.dataexport(login,password)
        pass
    except Exception as e:
        print(e)
    finally:
        command = input()
        if command == 'exit':
            driver.quit()
        # time.sleep(30)
        # driver.quit()


if __name__ == "__main__":
    main()
