from utils.duriel import *
from utils.web import *
driver.get('https://www.lagou.com/')
driver.find_element('xpath', '//*[@id="changeCityBox"]/p[1]/a').click()
driver.find_element('id', 'search_input').send_keys('python', Keys.ENTER)
time.sleep(2)
alink = driver.find_elements('class name', 'item-top__1Z3Zo')
alink[0].find_element('xpath', './div/div[1]/a').click()
win = driver.window_handles
driver.switch_to.window(win[-1])
print(win)
time.sleep(5)
jb = driver.find_element('class name', 'job-detail').text
print(jb)
time.sleep(1)
print(driver.page_source)
# driver.quit()
