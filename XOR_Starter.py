def main():
    #今回はX="label",y=13
    X = tuple(ord(i) for i in input("input string:"))
    y =int(input("input number:"))
    Z = []
    print(X)
    for x in X :
        Z.append(chr(x^y))
    ans = "crypto{"+"".join(Z)+"}"
    print(ans)

if __name__ == '__main__':
    main()