import socket
import os

def recData(connection):
    #参数
    r=0
    pairs_x=[]
    pairs_y=[]
    hash_1=[]
    y=[]
    ksi=0
    #接收pairs_x,pairs_y
    Flag=True
    while Flag:
        buf = str(connection.recv(1024).decode())
        if buf == "ok":
            connection,address = sock.accept()
            
        if buf=="pairs_x":
            buf = int(str(connection.recv(1024).decode()))
            pairs_x.append(buf)
        
        if buf=="pairs_y":
            buf = int(str(connection.recv(1024).decode()))
            pairs_y.append(buf)
        
        if buf=="r":
            buf = int(str(connection.recv(1024).decode()))
            r=buf
            
        if buf=="hash":
            buf = str(connection.recv(1024).decode())
            hash_1.append(buf)

        if buf=="ksi":
            buf = int(str(connection.recv(1024).decode()))
            ksi=buf
            
        if buf=="over":
            Flag=False
            connection.close()
            
    return (pairs_x,pairs_y,r,hash_1,ksi)
