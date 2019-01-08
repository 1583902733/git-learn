#Python3.6

from base64 import *
import random
basecode={
    '16':lambda x:b16encode(x),
    '32':lambda x:b32encode(x),
    '64':lambda x:b64encode(x)
    } #定义一个字典函数（三个关键字）

flag=input('Please input a string:').encode()
#注意要加 encode()；input()输入的是字符串；而base加解密函数要接受byte类型

i=0
while(i<10):  #用三种加密函数随机加密10次
    order=random.choice(['16','32','64']) 
    flag=basecode[order](flag)
    i+=1
    
with open("text.txt",'w') as fp:
    fp.write(flag.decode())


