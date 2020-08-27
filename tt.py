import socket
import time,threading
def tt1(tcp_port,tcp_heartbeat,receive):    #一个主线程模拟一个下位机，tcp_port端口,tcp_heartbeat心跳包,receive数据
    def doConnect(ip_port): #建立socket连接
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sk.connect(ip_port)
        except:
            pass
        return sk
    
    def heartbeats(sk): #心跳
        while True:
            msg = str(time.strftime("%Y-%m-%d %H:%M:%S"))
            try:
                heartbeat = tcp_heartbeat
                sk.sendall(bytes(heartbeat, 'utf8'))
            except socket.error:
                print(f'\r\nsocket error,do reconnect:{msg}')
                time.sleep(3)
                break
            except:
                print(f'\r\nother error occur:{msg}')
                time.sleep(3)
                break
            time.sleep(30)

    def rec_send(sk):   #接收数据并返回
        while True:
            msg = str(time.strftime("%Y-%m-%d %H:%M:%S"))
            try:
                cmd=receive
                sk.recv(1024)
                sk.sendall(cmd)
            except socket.error:
                print(f'\r\nsocket error,do reconnect:{msg}\n{receive}')
                time.sleep(3)
                break
            except:
                print(f'\r\nother error occur:{msg}\n{receive}')
                time.sleep(3)
                break
    ip_port = ('127.0.0.1', tcp_port)
    while True:
        sk = doConnect(ip_port)  # print('客户端启动：')
        t1=threading.Thread(target=heartbeats,args=(sk,))   #心跳线程
        t2=threading.Thread(target=rec_send,args=(sk,))     #收发线程
        t1.start()
        t2.start()
        t1.join()
        t2.join()

return1='1'
return2='2'
return3='3'
return4='4'
return5='5'
return6='6'
return7='7'
return8='8'
return9='9'
return10='0'
return11='a'
return12='b'
return13='c'
return14='d'
return15='e'
return16='f'
return17='g'

client1=threading.Thread(target=tt1,args=(8712,'-_-_-_-_21',return1,))
client2=threading.Thread(target=tt1,args=(8712,'-_-_-_-_22',return2,))
client3=threading.Thread(target=tt1,args=(8712,'-_-_-_-_23',return3,))
client4=threading.Thread(target=tt1,args=(8712,'-_-_-_-_24',return4,))
client5=threading.Thread(target=tt1,args=(8712,'-_-_-_-_25',return5,))
client6=threading.Thread(target=tt1,args=(8712,'-_-_-_-_26',return6,))
client7=threading.Thread(target=tt1,args=(8712,'-_-_-_-_27',return7,))
client8=threading.Thread(target=tt1,args=(8712,'-_-_-_-_28',return8,))
client9=threading.Thread(target=tt1,args=(8712,'-_-_-_-_29',return9,))
client10=threading.Thread(target=tt1,args=(8712,'-_-_-_-_30',return10,))
client11=threading.Thread(target=tt1,args=(8712,'-_-_-_-_31',return11,))
client12=threading.Thread(target=tt1,args=(8712,'-_-_-_-_32',return12,))
client13=threading.Thread(target=tt1,args=(8712,'-_-_-_-_33',return13,))
client14=threading.Thread(target=tt1,args=(8712,'-_-_-_-_34',return14,))
client15=threading.Thread(target=tt1,args=(8712,'-_-_-_-_35',return15,))
client16=threading.Thread(target=tt1,args=(8712,'-_-_-_-_36',return16,))
client17=threading.Thread(target=tt1,args=(8712,'-_-_-_-_37',return17,))
client1.start()
time.sleep(0.5)
client2.start()
time.sleep(0.5)
client3.start()
time.sleep(0.5)
client4.start()
time.sleep(0.5)
client5.start()
time.sleep(0.5)
client6.start()
time.sleep(0.5)
client7.start()
time.sleep(0.5)
client8.start()
time.sleep(0.5)
client9.start()
time.sleep(0.5)
client10.start()
time.sleep(0.5)
client11.start()
time.sleep(0.5)
client12.start()
time.sleep(0.5)
client13.start()
time.sleep(0.5)
client14.start()
time.sleep(0.5)
client15.start()
time.sleep(0.5)
client16.start()
time.sleep(0.5)
client17.start()
time.sleep(0.5)

client1.join()
client2.join()
client3.join()
client4.join()
client5.join()
client6.join()
client7.join()
client8.join()
client9.join()
client10.join()
client11.join()
client12.join()
client13.join()
client14.join()
client15.join()
client16.join()
client17.join()