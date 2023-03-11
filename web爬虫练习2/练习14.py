from utils.duriel import *
from utils.web import *
# with open('a.jpg', 'rb') as f:
#     img = f.read()
# print(chaojiying.PostPic(img, 1902))
url = 'https://www.chaojiying.com/user/login/'
# pic_url = url.split('/user')[0]
# r = rq.get(url, headers=head).content.decode('utf8')
# bf = BeautifulSoup(r, 'html.parser')
# login = bf.find('div', class_='login_form').find('img')['src']
# print(pic_url+login)
# with open('chaojiying/a.jpg', 'wb') as f:
#     r = rq.get(pic_url+login)
#     f.write(r.content)
# with open('chaojiying/a.jpg', 'rb') as f:
#     img = f.read()

driver.get(url)
img = driver.find_element('xpath', '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
print(chaojiying.PostPic(img, 1902)['pic_str'])
