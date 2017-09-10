import socket
import time
def sendResult(sk,restr_result):
    for i in restr_result:
        sk.send("result".encode())
        time.sleep(0.01)
        sk.send(bytes(str(int(i)).encode()))
    sk.send("over".encode())
