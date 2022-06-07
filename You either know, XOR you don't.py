def main():

    sign = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    X = tuple(i for i in bytes.fromhex(sign))
    key = "crypto{"
    Y = tuple(ord(i) for i in key)
    Z = X^Y
    print(Z)
    # Y =tuple(range(256))
    # Z =set()
    # FLAG=set()
    # for y in Y :
    #     z = "".join(chr(x^y) for x in X)
    #     Z.add(z)
    # for z in Z:
    #     if z.find("crypto") >= 0 :
    #         FLAG.add(z)
    #     else:
    #         continue
    # print(FLAG)


if __name__ == '__main__':
    main()
