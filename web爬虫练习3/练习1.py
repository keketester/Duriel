from utils.duriel import *
html = """
    <ul>
        <div>
            <li class="aaa"><a href="www.baidu1.com">diyige</a></li>
            <li class="bbb"><a href="www.baidu2.com">练习</a></li>
            <li class="bbb" id="12"><a href="www.baidu3.com">练习</a></li>
        </div>
    </ul>
"""
p = PyQuery(html)
print(p('.aaa'))  # . = class
print(p('.bbb a'))
print(p('#12 a'))
print(p('#12 a').attr('href'))
print(p('#12 a').text())
it = p('li a').items()
for i in it:
    print(i.text(), i.attr('href'))
# p('div').after(PyQuery('<div>练习111</div>'))
# print(p)
# p('div').append('<div>练习111</div>')
# print(p)
# p('.bbb').attr('class', 'ccc')
# print(p)
# p('.aaa').attr('id', '1')
# print(p)
# p('.aaa').remove_attr('id')
# print(p)
# p('.aaa').remove()
# print(p)
p('ul > div > li:nth-child(2)').eq(0).text()
p('ul > div > li:nth-child(2) > dd:contains(xxx)')


