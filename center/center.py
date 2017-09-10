import os
import time
import random
import pyDes
import binascii
import struct
import hashlib
from scipy.interpolate import lagrange
import client
def f(r,s):
    return r+s

def func(r,s):
    s_temp=str(s).encode('utf_8')
    m=hashlib.md5()
    # hashlib.sha1
    m.update(s_temp)
    data=m.hexdigest().encode('utf_8')
    r_bytes=int2bytes64(r)
    k = pyDes.des(r_bytes, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(data)
    int_des=int(d.hex(),16)
    return int_des

def int2bytes64(a):
    str1=bin(a)
    str2=str1[2:len(str1)]
    n=64-len(str2)
    str3=str2
    for i in range(0,n):
        str3="0"+str3
    bytes_8=struct.pack(">Q",int(str3))
    return bytes_8

def h(x,y,a):
    ans=0.0
    for i in range(len(y)):
        t=y[i]
        for j in range(len(y)):
            if i !=j:
                t*=(a-x[j])/(x[i]-x[j])
        ans +=t
    return ans

def chioceSigma(m,q,rho,t):
    sigma_temp=[]
    for i in range(1,q):
        sigma_temp.append(i)
    for i in range(0,m):
        del sigma_temp[0]
    for i in rho:
        sigma_temp.remove(i)
    sigma=[]
    for i in range(0,len(rho)+m-t):
        sigma.append(min(sigma_temp))
        del sigma_temp[0]
    return sigma


#参数
p=83
q=41
alpha=13
t=3
s=[3,4,123456781234567]
m=len(s)
rho=[11,12,13,14,15]
n=len(rho)
c=[21,96,87,14,16]
ksi=22
r=19#公开
y=[]

for i in c:
    y.append(func(r,i))

pairs_x=list(range(0,m))
pairs_x=pairs_x+rho#发送至用户

pairs_y=[]
for i in s:
    pairs_y.append(ksi+i)

pairs_y=pairs_y+y#发送至用户

sigma=chioceSigma(m,q,rho,t)
w_sigma=[]
for i in sigma:
    w_sigma.append(h(pairs_x,pairs_y,i))#公开w_sigma
    
#连接客户
for i in pairs_x:
    client.sendMessage("pairs_x".encode())
    client.sendMessage(bytes(str(i).encode()))

for i in pairs_y:
    client.sendMessage("pairs_y".encode())
    client.sendMessage(bytes(str(i).encode()))
    
client.sendMessage("r".encode())
client.sendMessage(bytes(str(r).encode()))

client.sendMessage("ksi".encode())
client.sendMessage(bytes(str(ksi).encode()))
#哈希值
s_1=[]
for i in s:
    i_tem=str(i).encode('utf_8')
    m=hashlib.md5()
    m.update(i_tem)
    s_1.append(m.hexdigest())
for i in s_1:
    client.sendMessage("hash".encode())
    client.sendMessage(bytes(str(i).encode()))
client.sendMessage("over".encode())
    
#公告栏    
print("--------------Bulletin Board--------------")
print("r=",r,"\n")
print("w_sigma:")
for i in w_sigma:
    print(i)
print("\nhash:")
for i in s_1:
    print(i)
print("------------------------------------------")


























