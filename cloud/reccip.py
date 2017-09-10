import socket
import os

def recCip(sk):
    encx=[]
    ency=[]
    
    Flag=True
    while Flag:
        buf=sk.recv(1024)
        if buf==b"over":
            Flag=False
        if buf==b"encx":
            buf=sk.recv(1024)
            encx.append(buf)
        if buf==b"ency":
            buf=sk.recv(1024)
            ency.append(buf)
    return (encx,ency)
