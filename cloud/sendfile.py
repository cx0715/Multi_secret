import socket,sys,os
import time

def sendFile(sk):
    Sign=True
    while True:
        file_path=os.path.join(os.getcwd(),"public.pem")
        file_name=os.path.basename(file_path)
        file_size=os.stat(file_path).st_size
        sk.send((file_name+"|"+str(file_size)).encode())
        time.sleep(2)
        send_size=0
        f=open(file_path,'rb')
        Flag=True
        while Flag:
            if send_size + 1024 > file_size:
                data = f.read(file_size - send_size)
                Flag = False
            else:
                data = f.read(1024)
                send_size += 1024
            sk.send(data)
        f.close()
        #sk.close()
        Sign=False
        return "File sent successfully"
    
