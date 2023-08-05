def main():
    print("Enter no: ")
    no = int(input())

    res = no % 2
    if(res == 0):
        print("even")
    else:
        print("odd")

if __name__ == "__main__":
    main()