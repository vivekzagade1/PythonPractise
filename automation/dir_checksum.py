import sys
import os
import hashlib


def hash_file(path, block_size=1024):
    a_file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = a_file.read(block_size)

    while len(buf) > 0:
        hasher.update(buf)
        buf = a_file.read(block_size)
    a_file.close()
    return hasher.hexdigest()


def display_checksum(path):
    flag = os.path.isabs(path)
    if not flag:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dir_name, sub_dir, file_list in os.walk(path):
            print("Current Folder is: " + dir_name)
            for file_n in file_list:
                path = os.path.join(dir_name, file_n)
                file_hash = hash_file(path)
                print(path)
                print(file_hash)
                print(" ")
    else:
        print("Invalid Path")


def main():
    print("-----------Marvellous Infosystems-----------")

    print("Application Name: " + sys.argv[0])

    if(len(sys.argv) != 2):
        print("Error: Invalid Argument")
        exit()

    if (sys.argv[1] in ['-h', '-H']):
        print("This automation script is used to traverse directory and display checksum")
        exit()
    if (sys.argv[1] in ['-u', '-U']):
        print("Usage: Name_of_Script absolute_path extension")
        exit()

    try:
        display_checksum(sys.argv[1])

    except ValueError:
        print("Invalid datatype of input")

    except Exception as e:
        print("Error: Invalid input", e)


if __name__ == '__main__':
    main()
