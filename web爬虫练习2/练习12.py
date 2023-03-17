from utils.web import *
from utils.duriel import *

driver = webdriver.Chrome(chrome_options=options)
# driver.maximize_window()
driver.get('https://www.lagou.com/')
driver.find_element('xpath', '//*[@id="changeCityBox"]/p[1]/a').click()
driver.find_element('id', 'search_input').send_keys('python', Keys.ENTER)
time.sleep(2)
item = driver.find_elements('class name', 'item-top__1Z3Zo')
for i in item:
    com = i.find_element('xpath', './div[2]/div[1]/a').text
    name = i.find_element('xpath', './div[1]/div[1]/a').text
    money = i.find_element('xpath', './div[1]/div[2]/span').text
    print(com, name, money)
driver.close()
