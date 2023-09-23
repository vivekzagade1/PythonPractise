from sys import *
import os
import time

def ReName(DirName, oldname):
    print("This Scrept is use to Rename the File name")
    
    flag = os.path.isfile(oldname)
    print(flag)
    oldname = os.path.abspath(oldname)
   
    DirName = os.getcwd() + "/" + DirName
    print(oldname)
    print(DirName)
    os.rename(oldname, DirName)

    # for foldername ,subfoldername,filename in os.walk(os.curdir()):

def main():

    if(len(argv) != 3):
        print("Invalid Path.....")
        exit()

    if(argv[1] == "-H" or argv[1] == "-h"):
        print("This automation script is used to perform File Automations")
        exit()
    
    elif(argv[1] == "-H" or argv[1] == "-h"):

        print("Usage : Name_Of_Script First_Argument Second_Argument")
        print("Example : Demo.py Marvellous.txt temp.txt")
        exit()

    starttime = time.time()
    ReName(argv[1], argv[2])
    endtime = time.time()

    print("Time requred for execution is : ",endtime-starttime)

if __name__ == "__main__":
    main()