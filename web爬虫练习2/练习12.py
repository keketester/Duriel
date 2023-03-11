import time

from utils.duriel import *

driver = webdriver.Chrome(chrome_options=options)
# driver.maximize_window()
driver.get('https://www.lagou.com/')
driver.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a').click()
driver.find_element_by_id('search_input').send_keys('python', Keys.ENTER)
time.sleep(2)
item = driver.find_elements_by_class_name('item-top__1Z3Zo')
for i in item:
    com = i.find_element_by_xpath('./div[2]/div[1]/a').text
    name = i.find_element_by_xpath('./div[1]/div[1]/a').text
    money = i.find_element_by_xpath('./div[1]/div[2]/span').text
    print(com, name, money)
driver.close()
