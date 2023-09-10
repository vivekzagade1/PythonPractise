import os.path


def main():
    print("Enter File name")
    file_name = input()

    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("File doesn't exist")


if __name__ == '__main__':
    main()
