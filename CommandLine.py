import sys

def main():
    
    print("Demonstration of Cmd Args")

    val1 = int(sys.argv[1])
    val2 = int(sys.argv[2])

    addi = val1 + val2

    print("Addition is ", addi)

if __name__ == "__main__":
    main()