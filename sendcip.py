import socket
import os

def sendCip(connection,encx,ency):
    for i in encx:
        connection.send(b'encx')
        connection.send(i)
    for i in ency:
        connection.send(b'ency')
        connection.send(i)
    connection.send(b'over')
