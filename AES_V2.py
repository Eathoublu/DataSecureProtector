# coding:utf8
from Crypto.Cipher import AES
import base64
import os
import hashlib


# cipher = AES.new('asdfgh7812345678')

# regist_code = cipher.decrypt('')
# cipher_2 = AES.new('asdfgh7812345678')


# miwen = base64.b64encode(cipher.encrypt('n  aoa7812345678'))

# mingwen = cipher_2.decrypt(base64.b64decode(miwen))


def get_text_prefix(text, PRE='[**#$$$#**-}-'):
    return PRE + text


def decode_validation(text, PRE='[**#$$$#**-}-'):
    if text[:len(PRE)] == PRE:
        return True
    return False


def make_text_ok_for_encode(text, multiple=16):
    if len(text) % multiple == 0:
        return text
    ws = len(text) % multiple
    # print('ws', ws)
    for _ in range(multiple - int(ws)):
        text += ' '
    return text


def check_name(name, folder='.aes_safe_save_data_folder'):
    return bool(os.path.exists(folder + '/' + name))


def get_origin_text(text, PRE='[**#$$$#**-}-'):
    return text[len(PRE):]


# print(mingwen)
BASE_DIR = os.path.expanduser('~/')+'.aes_safe_save_data_folder'

if __name__ == '__main__':
    #
    print("""
    欢迎使用密钥安全管理工具 by lanyixiao V1.0

               使用方法：
    1）新建一个私钥储存库 -》键入a
    2）查看已经储存的私钥 -》输入b
    """)
    # print(os.path.abspath(''))
    # os.mkdir('.data')
    if not os.path.exists(BASE_DIR):
        os.mkdir(BASE_DIR)
    #
    #
    while True:
        mode = raw_input('>>>')
        if mode == 'a':
            name = raw_input('>>>请输入一个储存库的名字:')
            while check_name(name):
                name = raw_input('>>>名字已经被占用！请再输入一个储存库的名字:')
            password = raw_input('>>>请输入一个储存库的密码(小于等于16):')
            password = make_text_ok_for_encode(password)
            # print(len(password))
            cipher = AES.new(password)
            text = raw_input('>>>请输入要储存的私钥:')
            encode = base64.b64encode(cipher.encrypt(make_text_ok_for_encode(get_text_prefix(text))))
            with open(BASE_DIR + '/' + name, 'wb') as f:
                f.write(encode)
                f.close()
            print('恭喜！已经安全保存至储存库！请牢记密码！')
        if mode == 'b':
            name = raw_input('>>>请输入想要查看的储存库的名字：')
            while not check_name(name):
                name = raw_input('>>>没有这个储存库！请检查后再输入:')
            password = raw_input('>>>请输入这个储存库的密码:')
            password = make_text_ok_for_encode(password)
            cipher = AES.new(password)
            with open(BASE_DIR + '/' + name, 'r') as f:
                content = f.read()
                f.close()
            text = cipher.decrypt(base64.b64decode(content))
            # print(text)
            while not decode_validation(text):
                print('>>>对不起！密码存在问题！请检查密码。')
                password = raw_input('>>>请输入这个储存库的密码:')
                password = make_text_ok_for_encode(password)
                cipher = AES.new(password)
                text = cipher.decrypt(base64.b64decode(content))
            print('恭喜！解码成功。如下：')
            print(get_origin_text(text))
            _ = raw_input('>>>按任意键继续')
        print("""
        1）新建一个私钥储存库 -》键入a
        2）查看已经储存的私钥 -》输入b
    """)

