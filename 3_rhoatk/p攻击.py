# 此处进行前8bit的碰撞以作演示
import random
from sm3 import sm3


def pa():
    num = 8     # 前8bit
    x_0 = hex(random.randint(0, 2**(num+1)-1))[2:]
    x_2 = x_1 = x_0
    x_1 = sm3(x_1)
    x_2 = sm3(sm3(x_2))
    cnt = 1
    while x_1[:int(num/4)] != x_2[:int(num/4)]:
        cnt += 1
        x_1 = sm3(x_1)
        x_2 = sm3(sm3(x_2))
    x_2 = x_2
    x_1 = x_0
    for j in range(cnt):
        if sm3(x_1)[:int(num/4)] == sm3(x_2)[:int(num/4)]:
            return [sm3(x_1)[:int(num/4)], x_1, x_2]
        else:
            x_1 = sm3(x_1)
            x_2 = sm3(x_2)


if __name__ == '__main__':
    m = pa()
    print("消息1:", m[1])
    print("消息2:", m[2])
    print("碰撞为:", m[0])