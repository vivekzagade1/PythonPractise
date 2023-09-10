import os.path


def main():
    print("Enter File name")
    file_name = input()

    if os.path.exists(file_name):
        fobj = open(file_name, "r")
        if fobj:
            print("File opened")

            line1 = fobj.readline()
            print(f"Line1: {line1}")

            data = fobj.read()
            print(f"data from file: {data}")

            fobj.close()
        else:
            print("Unable to open")
    else:
        print("File doesn't exist")


if __name__ == '__main__':
    main()
