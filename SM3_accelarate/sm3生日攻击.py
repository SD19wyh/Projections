# 演示前8bit的碰撞
def ba():
    exm = 8  # exm = 8bit
    num = int(2 ** (exm / 2))
    ans = {}
    for i in range(num):
        temp = sm3([str(i)])[0:int(exm / 4)]     #此处sm3没有给出具体函数
        if temp in ans:
            return [temp, ans[temp], i]
        else:
            ans[temp] = i


if __name__ == '__main__':
    print(ba())
