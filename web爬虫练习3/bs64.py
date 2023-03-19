from utils.duriel import *
s = 'base64'.encode('utf8')
s1 = base64.b64encode(s).decode('utf8')
print(s1)
s2 = base64.b64decode(s1).decode('utf8')
print(s2)