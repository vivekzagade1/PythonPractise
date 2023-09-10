import os.path


def main():
    print("Enter File name")
    file_name = input()

    if os.path.exists(file_name):
        fobj = open(file_name, "r")
        if fobj:
            print("File opened")
            fobj.close()
        else:
            print("Unable to open")
    else:
        print("File doesn't exist")


if __name__ == '__main__':
    main()
