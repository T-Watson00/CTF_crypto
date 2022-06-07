def main():

    sign = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    X = tuple(i for i in bytes.fromhex(sign))
    Y =tuple(range(256))
    Z =set()
    FLAG=set()
    for y in Y :
        z = "".join(chr(x^y) for x in X)
        Z.add(z)
    for z in Z:
        if z.find("crypto") >= 0 :
            FLAG.add(z)
        else:
            continue
    print(FLAG)

if __name__ == '__main__':
    main()