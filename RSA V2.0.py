# coding:utf8

# -*- coding: UTF-8 -*-
# from Crypto.
#
# (public_key, private_key) = rsa.newkeys(1024)
# print(chr(10)+"公钥：")
# print(public_key.save_pkcs1())
# print(chr(10)+"公钥：")
# print(public_key.save_pkcs1())

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import base64

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def get_rsa_key():
    random_generator = Random.new().read
    rsa = RSA.generate(1024, random_generator)
    private_key = rsa.exportKey()
    public_key = rsa.publickey().exportKey()
    return private_key, public_key


def decode(key, rsa_text):
    pri_key = RSA.importKey(key)
    cipher = PKCS1_cipher.new(pri_key)
    back_text = cipher.decrypt(base64.b64decode(rsa_text), 0)
    # print(back_text.decode('utf-8'))
    return back_text.decode('utf-8')


def encode(key, origin_text):
    pub_key = RSA.importKey(str(key))
    cipher = PKCS1_cipher.new(pub_key)
    rsa_text = base64.b64encode(cipher.encrypt(bytes(origin_text.encode("utf8"))))
    # print(rsa_text.decode('utf-8'))
    return rsa_text.decode('utf-8')


# pri, pub = get_rsa_key()

if __name__ == '__main__':

    # o = 'ofdireoiver'

    # r = encode(pub, o)
    # print(decode(pri, r))

    print("""               --* Hello *-- 
                   欢迎使用RSA安全数据传输脚本 by 蓝一潇
                               使用方法：

    1）键入a可以产生一个密钥对，将公钥发送给向你共享数据的人。（请不要多次按a，否则将改变私钥）
    2）键入b之后输入密文数据，便可以进行解密。
    """)

    mode = raw_input('>>>(a/b)?')

    if mode == 'a':
        pri, pub = get_rsa_key()
        with open('priKey.rsa', 'wb') as f:
            f.write(pri)
            f.close()
        print('您的rsa公钥如下，请发送给共享数据的人：\n' + pub)

    if mode == 'b':
        print('请复制密文，放置于此：')
        cry_text = raw_input('>>>')
        with open('priKey.rsa') as f:
            pri = f.read()
            f.close()
        origin = decode(pri, cry_text)
        print('明文如下：\n' + origin)
        # print('b')

    if mode == 'c':
        with open('pub.txt') as f:
            pub = f.read()
            f.close()
        # origin = raw_input('>>>')
        with open('origin.txt') as f:
            origin = f.read()
            f.close()
        print(encode(pub, origin))




