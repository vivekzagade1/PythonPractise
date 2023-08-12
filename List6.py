def main():
    print("Enter len: ")
    length = int(input())

    arr = list()

    print("Enter elements: ")
    for i in range(length):
        arr.append(input())

    k = 0
    while(k < length):
        print(arr[k])
        k+=1
    


if __name__ == "__main__":
    main()