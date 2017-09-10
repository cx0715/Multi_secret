import socket

sk=socket.socket()
sk.connect(('localhost',8888))

def sendMessage(message):
    sk.send(message)
