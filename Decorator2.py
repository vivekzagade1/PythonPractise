# Inbuilt function
def sub(a, b):   # 0x0100
    return a - b


# Decorator
def smartSub(FPTR):   # 0x200
    def inner(a, b):  # 0x300
        if(a < b):
            a, b = b, a
        return FPTR(a, b)    # return 0x100
    return inner             # return 0x300


def main():

    subx = smartSub(sub)   # 0x200(0X100)

    ret = subx(10, 7)     # 0x300(10, 7)
    print(ret)

    ret = subx(7, 10)     # 0x300(10, 7)
    print(ret)


if __name__ == '__main__':
    main()
