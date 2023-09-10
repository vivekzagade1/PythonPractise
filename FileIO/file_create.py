import os.path


def main():
    print("Enter File name")
    file_name = input()

    if os.path.exists(file_name):
        print("File exists")
    else:
        fobj = open(file_name, "x")


if __name__ == '__main__':
    main()
