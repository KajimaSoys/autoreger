import random

# Параметры для прокси
username = 'http://lum-customer-hl_79a92981-zone-static'
password = 'f9ad1zb48xxp'#password
port = 22225


# Рандомим новую сессию для прокси
def newSession():
    return random.random()


# Получаем новые прокси
def proxyBuilder():
    session_id = newSession()
    #http://%s-country-ru-session-%s:%s@zproxy.lum-superproxy.io:%d
    super_proxy_url = ('http://%s-country-ru:%s@zproxy.lum-superproxy.io:%d' %
                       (username, password, port))
    proxy_handler = {
        #'http': super_proxy_url,   Это варианты для реквестов
        #'https': super_proxy_url,

    }
    proxy_handlerTEST=super_proxy_url
    return proxy_handlerTEST

print(proxyBuilder())