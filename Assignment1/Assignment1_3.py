def add():
    no1 = float(input("Enter 1st no: "))
    no2 = float(input("Enter 2st no: "))
    
    if(no1.is_integer() and no2.is_integer()):
        return int(no1 + no2)    
    return no1 + no2

def main():
    res = add()
    print(res)


if __name__ == "__main__":
    main()