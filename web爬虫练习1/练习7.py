import re

s = """<div class='三国演义'><span id='1'>张飞</span></div>
       <div class='西游记'><span id='2'>孙悟空</span></div>
       <div class='水浒传'><span id='3'>宋江</span></div>
       <div class='红楼梦'><span id='4'>林黛玉</span></div>
"""

obj = re.compile(r"<div class='(?P<mingzhu>.*?)'><span id='(?P<id>.*?)'>(?P<name>.*?)<.*?", re.S)
r = obj.findall(s)
print(r)

r1 = obj.finditer(s)
for i in r1:
    print(i.group('mingzhu', 'id', 'name'))
    print(i.groups())
