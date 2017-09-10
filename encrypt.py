import rsa
import pyDes
from scipy.interpolate import lagrange

#加载公钥
with open('public.pem','r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
    
#加密
def rsaEncrypt(str):
    #明文编码格式
    content=str.encode("utf8")
    #公钥加密
    crypto=rsa.encrypt(content,pubkey)
    return crypto

    
    
