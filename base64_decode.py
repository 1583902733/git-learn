#Python3.6

from base64 import *
import binascii

'''因为对用base64加密的数据用base32或base16解密几乎是不可能成功的，同base32;
    所以依次尝试使用base16、base32、base64进行解密'''

#Define a function to decode the code...
def decode_fun(code):
    try:
        decode=b16decode(code)
        return decode
    except binascii.Error:
        pass

    try:
        decode=b32decode(code)
        return decode
    except binascii.Error:
        pass

    try:
        decode=b64decode(code)
        return decode
    except binascii.Error:
        pass

def main():
    with open('text.txt','r') as fp:
        code=fp.read().encode()
    i=0
    while(i<10):
        code=decode_fun(code)
        i+=1
    print('The string is:'+ code.decode())

if __name__ == '__main__':
    main()


