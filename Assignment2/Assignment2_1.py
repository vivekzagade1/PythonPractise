import sys
import Arithematic


def main():
    if(sys.argv[1] and sys.argv[2]):
        op1 = float(sys.argv[1])
        op2 = float(sys.argv[2])
        print('Add is: ', Arithematic.Add(op1, op2))
        print('Sub is: ', Arithematic.Sub(op1, op2))
        print('Mul is: ', Arithematic.Mult(op1, op2))
        print('Div is: ', Arithematic.Div(op1, op2))
    else:
        print('Insufficient Args')
    

if __name__ == "__main__":
    main()