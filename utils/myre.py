# import re
# a = 'Asdh\na65Asfkj8a\nsd8asda99fa_jhj8a&7687a 3a\tdf'
# r = re.split('\\d+', a)
# r2 = re.findall('a\\S', a, re.I | re.S)
# r4 = re.findall('a.', a, re.I | re.S)
# r5 = re.findall('^a.', a, re.I | re.S)
# r6 = re.findall('\\w+$', a, re.I | re.S)
# r7 = re.findall('as*', a, re.I | re.S)
#
# r1 = re.sub('\\d+', ' ** ', a)
# r3 = re.sub('\\s+', ' ** ', a)
# '''\\w匹配单词 字母数字下划线
#     \\W匹配非单词
#     \\d匹配数字字符
#     \\D匹配非数字字符
#     \\s匹配空白字符
#     \\S匹配非空白字符
#     .匹配除换行符以外任意字符
#     ^匹配字符串开头
#     $匹配字符串结尾
#     *匹配前一个字符任意次
#     +匹配前一个字符至少一次
#     ?匹配前一个字符0次或1次
#     {n}匹配前一个字符n次
#     {n,}匹配前一个字符至少n次
#     {n,m}匹配前一个字符n到m次
#     {,m}匹配前一个字符最多m次'''
