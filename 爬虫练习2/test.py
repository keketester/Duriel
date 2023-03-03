from Crypto.Cipher import AES
from utils.duriel import Edcryp
a = '电话是'
b = ['我的','13213131']
print(a.join(b))

data = {
    "agent_num": "700000004",
    "username": "15334555345",
    "password": "123456",
    "id": "GCCC73256CB25DAF946257A026803BA96A26BDBC2384085030D",
    "tn": "T2gA18z9P1DSP5KiRpiYVL9rT_IAK2xkU_UPIpBVsD1Xqdi4Dqmsx65Hxvz_Icw1Djo="
}

a = Edcryp.encrypt(data,'asftgh78ju1edghj','0b196e85544cc8e9')
print(a)

