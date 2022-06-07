from binascii import unhexlify

def main():
    KEY1 = int("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313",16)
    KEY2_KEY1 = int("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e",16)
    KEY2_KEY3 = int("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1",16)
    FLAG_KEY1_KEY2_KEY3 = int("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf",16)
    KEY2 = KEY2_KEY1^KEY1
    KEY3 = KEY2^KEY2_KEY3
    FLAG = hex(FLAG_KEY1_KEY2_KEY3^KEY1^KEY2^KEY3)[2:]
    ans = unhexlify(FLAG).decode("utf-8")
    print(ans)


if __name__ == '__main__':
    main()