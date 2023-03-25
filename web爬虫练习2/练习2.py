from utils.duriel import *
from lxml import etree

xml = """
<book>
    <p>
    <name>haha</name>
        <name>keke</name>
        <name>duriel</name>
        <name>baer</name>
        <name>向可</name>
        <info>
            <name>墨菲斯托</name>
            <age>29</age>
                <birth>1102</birth>
            <weight>137</weight>
        </info>
    </p>
</book>
"""
tree = etree.XML(xml)
res = tree.xpath("/book/p//name/text()")
res1 = tree.xpath("/book/p/*/name/text()")
res2 = tree.xpath("/book//name/text()")
res3 = tree.xpath("/book//name[contains(@class, 'asd')]")
print(res1)
