import socket
import encrypt
import os
import recdata
import recfile
import proving
import encrypt
import sendcip
import recresult

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8888))
sock.listen(5)

#接收pairs_x,pairs_y,r
connection,address = sock.accept()
print("center connectied...\n")
(pairs_x,pairs_y,r,hash_1,ksi)=recdata.recData(connection)

print("Data received")

#接收公钥
connection,address = sock.accept()
print("\ncloud connectied...\n")
recfile.recFile(connection)


#加密并上传至云
encx=[]
ency=[]
#connection,address = sock.accept()
for i in pairs_x:
    crypto=encrypt.rsaEncrypt(str(i))
    encx.append(crypto)
for i in pairs_y:
    crypto=encrypt.rsaEncrypt(str(i))
    ency.append(crypto)
sendcip.sendCip(connection,encx,ency)

print("\n-------------------Result-------------------")

restr_result=recresult.recResult(connection)

result=[]
for i in restr_result:
	result.append(int(i-ksi))
	print(int(i-ksi))

#验证
proving.provhash(hash_1,result)
