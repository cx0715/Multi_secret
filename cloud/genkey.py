import rsa
import pyDes
import hashlib


#生成并保存公钥、私钥
(pubkey, privkey) = rsa.newkeys(1024)
with open('public.pem','w+') as f:
    f.write(pubkey.save_pkcs1().decode())
with open('private.pem','w+') as f:
    f.write(privkey.save_pkcs1().decode())
