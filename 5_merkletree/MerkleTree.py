import hashlib
import string
import random


def gen_str(length):
    res = []
    for k in range(length):
        res.append(random.choice(string.digits + string.ascii_letters))
    return ''.join(res)


# 确定哈希函数
def hash_ch(x, hash_change='sha256'):
    hash_change = getattr(hashlib, hash_change)  # 哈希方式为sha256
    x = x.encode("utf-8")  # 进行二进制编码
    return hash_change(x).hexdigest()


# 计算merkle tree
def merkle(str_l):
    length = len(str_l)
    if length == 0:
        return hash_ch('')
    elif length == 1:  # 只有一个结点时，输出sha256(‘0x00’+str_l[0])
        return hash_ch(chr(int('0x00', 16)) + str_l[0])
    else:
        index = 2 ** (len(bin(length - 1)) - 3)  # 根据树的性质寻找递归树中的分点
        left_t = merkle(str_l[index])  # 左子问题
        right_t = merkle(str_l[index:])  # 右子问题
        return hash_ch(chr(int('0x01', 16)) + left_t + right_t)


if __name__ == '__main__':
    block_l = []
    for i in range(100000):
        random_str = gen_str(8)
        block_l.append(random_str)
    print("Merkle Tree‘s root note:", merkle(block_l))
