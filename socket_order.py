

def split_order(device_id: str, order: str, param: str, **kwargs):
    """
    拼接指令
    """
    HEAD = "AA333380"
    HEAD_BYTES = bytes.fromhex(HEAD)

    TAIL = "FCFF"
    TAIL_BYTES = bytes.fromhex(TAIL)

    device_id_bytes = bytes.fromhex(str(device_id))
    if len(device_id_bytes) != 8:
        print("设备码的长度不对！")
        return

    order_bytes = bytes.fromhex(str(order))
    if len(order_bytes) != 2:
        print("命令的长度不对！")
        return

    other_param = ''.join(kwargs.values())

    param = param + other_param

    param_bytes = bytes.fromhex(str(param))

    order_len = (2 + len(device_id_bytes) +
                 len(order_bytes) + len(param_bytes) + 2 + 2)
    print("参数长度：" + str(len(param_bytes)))
    order_len_hex = "{:04x}".format(order_len)
    print("指令长度：" + order_len_hex)

    crc16_data = HEAD + order_len_hex + device_id + order + param
    print("未加校验和尾：" + crc16_data)

    crc16_code = crc16(bytearray.fromhex(crc16_data))

    data_packet = crc16_data + crc16_code + TAIL

    return data_packet


def crc16(x, invert=False):
    """ 
    x：bytearray.fromhex("bb6666")
    invert:翻转 false 
    """
    wCRCin = 0x0000  # 初始值
    wCPoly = 0x1021  # 多项式 POLY
    for byte in x:
        if type(byte) is str:
            # 这里做了个判断可以直接传入字符串，但存在意义不大
            wCRCin ^= (ord(byte) << 8)
        else:
            wCRCin ^= ((byte) << 8)
        for i in range(8):
            if wCRCin & 0x8000:
                wCRCin = (wCRCin << 1) ^ wCPoly
            else:
                wCRCin = (wCRCin << 1)

    s = hex(wCRCin).upper()

    return s[-2:] + s[-4:-2] if invert == True else s[-4:-2] + s[-2:]


device_id = "2222222211212121"
# order = "0007"

# 上传心跳
print("上传心跳，。，，。，。")
print(split_order(device_id=device_id,
                  order="0011",
                  param="9901"))

print("*-*-*-*-*-*-*-*-*-*-*-*")

# 上传消费记录
print("上传消费记录....")
print(split_order(
    device_id=device_id,
    order="0005",
    param="00000033",
    shuiwen="01",
    mode='0B',
    cklount='0123'))
print("*-*-*-*-*-*-*-*-*-*-*-*")

# 上传设备耗材数据
print("上传设备耗材数据...")
print(split_order(device_id=device_id,
                  order="0007",
                  param="00000002",
                  limit_surplus="00000000",
                  sp1="0100000000",
                  sp2="0000000000",
                  sp3="0000000000",
                  sp4="0000000000",
                  sp5="0000000000",
                  sp6="0000000000"))

# bb666680 0015 2222222211212121 0005 000000000 966c ffcff


# 上传 TDS
""" print(split_order(
        device_id=device_id,
        order="0002",
        param="",
        chun="",
        bingwen="",
        wenwen="",
        kaiwen="",
        other="000000")) """


# 设备上传心跳指令
# 频率：30s
# order：0012
# param[0]：0-255循环
# param[1]:01空闲、01运行、02结束

# 上传水机运行状态
# 开机发一次。状态改变也发一次
# order：0001
# parma[0]：00待机、0A运行、。。。。
# parma[1]：保留

# 上传消费记录
# order：0005
# param[:4]：********服务器下发的流水号
# param[4]：01热水、02温水、03冰水
# param[5]：0B脉冲、0C时间
# param[6:8]：****消费水的总量
