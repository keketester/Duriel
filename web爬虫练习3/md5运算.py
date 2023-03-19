from utils.duriel import *
add = b'asdahkhl'
md = md5(add)
password = 'kkkkk'
md.update(password.encode('utf8'))
miwen = md.hexdigest()
print(miwen)