# -*-coding:utf-8-*-

# socket 服务端和客户端    服务端监听   客户端的请求  链接确认

import socket
import threading
import time

outString = ''
inString = ''
nick = ''

# 发送信息的函数


def DealOut(sock):
    global nick, outString  # 声明为全局变量，进行赋值,这样才可以生效
    while True:
        outString = input()  # 输入
        # outString = nick+':'+outString  # 拼接cd
        sock.send(bytes.fromhex(outString))  # 发送


def xt(sock, cmd, sec=5.0):
    while True:
        time.sleep(sec)
        print('发送：' + cmd.hex(" "))
        sock.send(cmd)  # 发送


# 接收信息
def DealIn(sock):
    global inString
    while True:
        try:
            inString = sock.recv(1024)
            if not inString:
                break
            if outString != inString:
                print("接收到：", end=' ')
                print(inString.hex(' '))
        except:
            break


# nick = input('input your nickname:')#名字
xintiao = bytes.fromhex(
    'AA3333800018222222221121212100050000000b010B0123521FFCFF')

# xintiao = b'\xaa33\x80\x00\x18""""\x11!!!\x00\x05\x00\x00\x00\x0b\x01\x0b\x01#R\x1f\xfc\xff'
# xintiao.to_bytes(,byteorder='big')
ip = '39.98.135.128'  # raw_input('input your server ip address:')#ip地址

print(type(xintiao))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字,默认为ipv4
sock.connect((ip, 60021))  # 发起请求，接收的是一个元组
# sock.send(nick.encode('utf8'))
sock.send(xintiao)


# 多线程  接收信息 发送信息
thin = threading.Thread(target=DealIn, args=(sock,)
                        )  # 调用threading 创建一个接收信息的线程'
thin.start()

thxt = threading.Thread(target=xt, args=(sock, xintiao, 30)
                        )  # 调用threading 创建一个接收信息的线程'
thxt.start()

thout = threading.Thread(target=DealOut, args=(sock,))  # 创建一个发送信息的线程，声明是一个元组
thout.start()

#
