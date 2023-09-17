import sys
import arithematic


def main():
    print("-----------------------Automation Script Marvellous Infosystem----------------")
    print(sys.argv[0])

    if(len(sys.argv) == 2):
        if(sys.argv[1] in ['-h', '-H']):
            print("This automation script is used to perform addition")
            exit()
        elif (sys.argv[1] in ['-u', '-U']):
            print("Usage: Name_of_Script argv1 argb2")
            print("Demo 10 11")
            exit()
        else:
            print("There is no such option")

    if (len(sys.argv) != 3):
        print("Invalid number of arguments")
        exit()
    else:
        ret = arithematic.addition(int(sys.argv[1]), int(sys.argv[2]))
        print(ret)


if __name__ == '__main__':
    main()
