import sys

def Add(oper1, oper2):
    op1 = float(oper1)
    op2 = float(oper2)

    if(op1.is_integer() or op1.is_integer()):
        return int(op1) + int(op2)
    else:
        return op1 + op2


def Sub(oper1, oper2):
    op1 = float(oper1)
    op2 = float(oper2)

    if(op1.is_integer() or op1.is_integer()):
        return int(op1) - int(op2)
    else:
        return op1 - op2


def Mult(oper1, oper2):
    op1 = float(oper1)
    op2 = float(oper2)

    if(op1.is_integer() or op1.is_integer()):
        return int(op1) * int(op2)
    else:
        return op1 * op2


def Div(oper1, oper2):
    op1 = float(oper1)
    op2 = float(oper2)

    if(op1.is_integer() or op1.is_integer()):
        return int(op1) / int(op2)
    else:
        return op1 / op2


def main():
    if(sys.argv[1] and sys.argv[2]):
        op1 = float(sys.argv[1])
        op2 = float(sys.argv[2])
        print('Add is: ', Add(op1, op2))
        print('Sub is: ', Sub(op1, op2))
        print('Mul is: ', Mult(op1, op2))
        print('Div is: ', Div(op1, op2))
    else:
        print('Insufficient Args')
    

if __name__ == "__main__":
    main()