import os
import rsa
import pyDes
import socket
import hashlib
import sendfile
import reccip
import decrypt
import h
import sendresult

sk=socket.socket()
sk.connect(('localhost',8888))

os.popen("genkey")  #生成并保存密钥
print(sendfile.sendFile(sk))#把公钥发送给用户

encx,ency=reccip.recCip(sk)#接收密文

#解密并重构
decx=[]
decy=[]
for i in encx:
    decx.append(int(decrypt.rsaDecrypt(i)))
for i in ency:
    decy.append(int(decrypt.rsaDecrypt(i)))

restr_result=[]
for i in range(0,3):
    restr_result.append(h.h(decx,decy,i))

sendresult.sendResult(sk,restr_result)
print("Result has been sent")

