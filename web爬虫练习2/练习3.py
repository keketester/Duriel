from utils.duriel import *

tree = etree.parse("p.html", parser=parser)
t = tree.xpath("/html/head/title/text()")
print(t)

t = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")
print(t)

t = tree.xpath("/html/body/ol/li/a/text()")
print(t)

t = tree.xpath("/html/body/ol/li")
print(t)

for i in t:
    print(i.xpath("./a/text()"))
for i in t:
    print(i.xpath("./a/@href"))

t = tree.xpath("/html/body/ul/li/a/@href")
print(t)

t = tree.xpath("/html/body/div[1]/text()")
print(t)