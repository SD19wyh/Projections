import sm3


def len_ext_atk(m, e, e_length):
    if len(e) % 128 < 112:
        e = e + '8' + '0' * (112 - len(e) % 128 - 1) + e_length
    else:
        e = e + '8' + '0' * (128 - len(e) % 128 - 1 + 112) + e_length
    E = sm3.Group(e)
    n = len(E)
    hm = sm3.sm3(m)
    Hm = [0] * 8
    for i in range(8):
        Hm[i] = int(hm[i * 8:i * 8 + 8], 16)
    V = []
    V.append(Hm)
    for i in range(n):
        V.append(sm3.CF(V, E, i))
    return V[n]


if __name__ == '__main__':
    m = '616263'
    e = '61'
    cnt = 0
    while len(m) >= 128:
        m = m[128:]
        cnt += 128
    if len(m) < 112:
        cnt += 128
    else:
        cnt += 256
    m_length = hex(len(m) * 4)[2:]  # 原消息长度
    m_length = (16 - len(m_length)) * '0' + m_length
    e_length = hex((cnt + len(e)) * 4)[2:]  # 总消息长度
    e_length = (16 - len(e_length)) * '0' + e_length
    extend_m = m + '8' + (cnt - len(m) - 17) * '0' + m_length + e  # 新消息=原消息+1000...+原消息长度+扩展消息
    res1 = sm3.sm3(extend_m)
    Vn = len_ext_atk(m, e, e_length)
    res2 = ''
    for x in Vn:
        res2 += hex(x)[2:]
    if res1 == res2:
        print("success!")