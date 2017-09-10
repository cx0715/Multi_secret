import hashlib


def provhash(hash_1,result):
    hash_2=[]
    for i in result:
        i_tem=str(i).encode('utf_8')
        m=hashlib.md5()
        m.update(i_tem)
        hash_2.append(m.hexdigest())
    print("----------------Verification----------------")
    for i in range(0,len(result)):
        if (hash_1[i]==hash_2[i]):
            print(hash_2[i],"  true")
        else:
            print(hash_2[i],"  false")
    print("---------------------------------------------")
