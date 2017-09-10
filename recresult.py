import socket

def recResult(connection):
    result=[]
    Flag=True
    while Flag:
        buf = str(connection.recv(1024).decode())
        if buf=="result":
            buf = int(str(connection.recv(1024).decode()))
            result.append(buf)
        if buf =="over":
            Flag=False
            connection.close()
    return result
