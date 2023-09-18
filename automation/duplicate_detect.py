import hashlib
import os
import sys


def hash_file(path, block_size=1024):
    a_file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = a_file.read(block_size)

    while len(buf) > 0:
        hasher.update(buf)
        buf = a_file.read(block_size)
    a_file.close()
    return hasher.hexdigest()


def find_duplicate(path):
    flag = os.path.isabs(path)
    if not flag:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dir_name, sub_dir, file_list in os.walk(path):
            # print("Current Folder is: " + dir_name)
            for file_n in file_list:
                path = os.path.join(dir_name, file_n)
                file_hash = hash_file(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid Path")


def print_duplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates Found, the duplicates are: ")

        count = 0
        for result in results:
            print(result)

    else:
        print("No duplicates")


def main():
    print("-------------Marvellous Infosystems---------------")
    
    print("Application name: " + sys.argv[0])
    
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
        arr = {}
        arr = find_duplicate(sys.argv[1])
        print_duplicate(arr)
        
    except ValueError:
        print("Error: Invalid datatype of input")


if __name__ == '__main__':
    main()
