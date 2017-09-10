import socket
import os

def recFile(connection):
    Sign=True
    while Sign:

        #获取文件名，文件大小
        file_info=str(connection.recv(1024).decode())
        file_name,file_size=file_info.split("|")

        recv_size=0
    
        #保存文件路径
        file_path=os.path.join(os.getcwd(),file_name)
    
        f=open(file_path,'wb')
        Flag=True
        while Flag:
            if int(file_size)>recv_size:
                data = connection.recv(1024)
                recv_size += len(data)
            else:
                recv_size = 0
                Flag = False
                continue
            #写入文件
            f.write(data)
        f.close()
        #connection.close()
        Sign=False
    print("PublicKey download successfully")
    print("FileName:",file_name,"\nFileSize:",file_size,"bytes")
