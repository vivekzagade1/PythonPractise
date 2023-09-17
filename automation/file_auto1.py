import os
import sys


def directory_travel(dir_name):
    print(f"we are going to traverse {dir_name}")

    for folder_name, sub_folder_name, filename in os.walk((dir_name)):
        print(f"Folder Name: {folder_name}, SubFolder name: {sub_folder_name},Filename: {filename}")
        for fname in filename:
            print(fname)


def main():
    print('-----------------------File Automation Script Marvellous Infosystem----------------')
    print(sys.argv[0])

    if (len(sys.argv) != 2):
        print("Invalid number of arguments")

    if(sys.argv[1] in ['-h', '-H']):
        print("This automation script is used to perform File Automation")
        exit()
    elif (sys.argv[1] in ['-u', '-U']):
        print("Usage: Name_of_Script argv1")
        print("demo.py marvellous")
        exit()
    else:
        # logic
        directory_travel(sys.argv[1])


if __name__ == '__main__':
    main()
