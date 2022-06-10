import ecdsa
import random
import hashlib


if __name__ == "__main__":
    gen = ecdsa.NIST256p.generator
    order = gen.order()
    # 生成私钥d_A
    d_A = random.randrange(1, order - 1)
    # 生成公私钥对象
    public_key = ecdsa.ecdsa.Public_key(gen, gen * d_A)
    private_key = ecdsa.ecdsa.Private_key(public_key, d_A)
    message = "message"
    m = int(hashlib.sha1(message.encode("utf8")).hexdigest(), 16)
    # 临时密钥
    k = random.randrange(1, order - 1)
    # 签名
    signature = private_key.sign(m, k)
    r = signature.r
    s = signature.s

    print(public_key.point.x(), public_key.point.y())
    a = ecdsa.ecdsa.Signature(r, s)
    b = a.recover_public_keys(m, gen)
    print(b[0].point.x(), b[0].point.y())
    print(b[1].point.x(), b[1].point.y())
    print("恢复公钥成功.")