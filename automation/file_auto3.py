import os
import sys
import time


def directory_travel(dir_name):
    print(f"we are going to traverse {dir_name}")

    flag = os.path.isabs(dir_name)

    if not flag:
        dir_name = os.path.abspath(dir_name)

    if os.path.isdir(dir_name):
        for folder_name, sub_folder_name, filename in os.walk((dir_name)):
            # print(f"Folder Name: {folder_name}, SubFolder name: {sub_folder_name},Filename: {filename}")
            for fname in filename:
                print(os.path.abspath(fname))
                print(f"{os.stat(fname).st_size} bytes")
    else:
        print("invalid path")


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
        start_time = time.time()
        directory_travel(sys.argv[1])
        end_time = time.time()

        print(f"The script too {end_time - start_time}")


if __name__ == '__main__':
    main()
