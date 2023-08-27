def acceptnumber():
    no = int(input("Enter nos of Elements: "))
    nos = []

    for i in range(0, no):
        nos.append(int(input(f"Enter the {i} element: ")))

    bignumber = nos[0]

    for i in range(0, no):
        if bignumber > nos[i]:
            bignumber = nos[i]

    print(bignumber)


def main():
    acceptnumber()


if __name__ == "__main__":
    main()

---------------

import multiprocessing
import os

def task1(value):
    print("Task2: Executing the first task  ")
    print('PDI of Running Process is ', os.getpid())
    print('Task1 PPID of Running Process is ', os.getppid())
    for i in range(value):
        print("Task1: ", i)



def task2(value):
    print("task2: Executing the second task  ")
    print('PDI of Running Process is ', os.getpid())
    print('Task2 PPID of Running Process is ', os.getppid())
    for i in range(value):
        print("Task2: ", i)

def main():
    print('Demo Multiprocessing')
    #print('Main PPID of Running Process is ', os.getppid())
    print('PDI of Running Process is ', os.getpid())

    no1 = 500
    no2 = 800
    p1 = multiprocessing.Process(target=task1, args=(no1, ))
    p2 = multiprocessing.Process(target=task2, args=(no2, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()


----------------


from functools import reduce

def Add(a, b):
    return a+b

def acceptNos():
    no = int(input("Enter nos of Elements: "))
    nos = []

    for i in range(0, no):
        nos.append(int(input(f"Enter the {i} element: ")))

    res = reduce(Add, nos)

    print(res)

def main():
    acceptNos()


if __name__ == "__main__":
    main()



------------------

import multiprocessing
import os

def task1(value):
    print("Task2: Executing the first task  ")
    print('PDI of Running Process is ', os.getpid())
    print('Task1 PPID of Running Process is ', os.getppid())
    for i in range(value):
        print("Task1: ", i)



def task2(value):
    print("task2: Executing the second task  ")
    print('PDI of Running Process is ', os.getpid())
    print('Task2 PPID of Running Process is ', os.getppid())
    for i in range(value):
        print("Task2: ", i)

def main():
    print('Demo Multiprocessing')
    #print('Main PPID of Running Process is ', os.getppid())
    print('PDI of Running Process is ', os.getpid())

    no1 = 500
    no2 = 800
    p1 = multiprocessing.Process(target=task1, args=(no1, ))
    p2 = multiprocessing.Process(target=task2, args=(no2, ))

    p1.start()
    p1.join()

    p2.start()
    p2.join()


if __name__ == "__main__":
    main()


-------------




def acceptnumber():
    no = int(input("Enter nos of Elements: "))
    nos = []

    for i in range(0, no):
        nos.append(int(input(f"Enter the {i} element: ")))

    bignumber = nos[0]

    count = 0
    searchElement = int(input("Elemtn to seach: "))
    for i in range(len(nos)):
        if(nos[i] == searchElement):
            count += 1
    print(count)


def main():
    acceptnumber()


if __name__ == "__main__":
    main()



--------------------------



from functools import reduce

def CheckEven(no):
    if(no%2 == 0):
        return True
    else:
        return False


def Increase(no):
    return no+2


def Add(a, b):
    return a+b

def main():
    data = [5, 4, 9, 8, 13, 17, 12, 18]
    print(data)

    filterData = list(filter(CheckEven, data))
    print(filterData)

    mapData = list(map(Increase, filterData))
    print(mapData)

    reducedData = reduce(Add, mapData)
    print(reducedData)


if __name__ == "__main__":
    main()


----------------------


def acceptNos():
    no = int(input("Enter nos of Elements: "))
    nos = []

    for i in range(0, no):
        nos.append(int(input(f"Enter the {i} element: ")))

    bigeNo = nos[0]

    for i in range(0, no):
        if(bigeNo < nos[i]):
            bigeNo = nos[i]

    print(bigeNo)

def main():
    acceptNos()


if __name__ == "__main__":
    main()


--------------------------

def DisplayModule2():
    print("Special variable of Module2.py is ", __name__)


--------------------------

import multiprocessing
import os

def task1():
    print("Task2: Executing the first task  ")
    print('PDI of Running Process is ', os.getpid())
    print('Task1 PPID of Running Process is ', os.getppid())


def task2():
    print("task2: Executing the second task  ")
    print('PDI of Running Process is ', os.getpid())
    print('Main PPID of Running Process is ', os.getppid())


def main():
    print('Demo Multiprocessing')
    print('PDI of Running Process is ', os.getpid())

    print('Main PPID of Running Process is ', os.getppid())
    task1()
    task2()

if __name__ == "__main__":
    main()


--------------------------------


def is_leap(year):
    leap = False

    if year%4==0:

        if year%100==0 and year%400==0:
            leap = True
        elif year%100:
            leap = False

        leap = True

    # Write your logic here

    return leap

year = int(input())
print(is_leap(year))



------------------------------

def DisplayModule1():
    print("Special variable of Module2.py is ", __name__)


------------------------

class HDFC:
    ROI = 9.5  # Class Variable

    def __init__(self, name, val1) -> None:  # Constructor
        self.balance = val1  # Instance Variable
        self.Accname = name
        print("Welcome ", self.Accname)
        print("Account gets created with balance: ", self.balance)

    def DisBal(self):  # Instance method
        print("Balance is : ", self.balance)

    @classmethod
    def displayeBankInfo(cls):  # Class Variable
        print("Welcome to HDFC variable")
        print("Out Bank is PVT bank")
        print("we provide, ROI", cls.ROI)

    @staticmethod
    def DisKYCInfo():
        print("According to RBI KYC doc are \n Aadhar \n PAN Card")

    def withDraw(self, val1):  # Instance method
        if self.balance < val1:
            print("Insuffiecient Funds")
        else:
            self.balance = self.balance - val1
            print("Amount withdrew success")

    def deposit(self, val1):  # Instance method
        self.balance += val1
        print("Deposit success")


def main():
    print("ROI os HDFC is ", HDFC.ROI)

    HDFC.displayeBankInfo()

    HDFC.DisKYCInfo()

    print("Createnew account")
    obj1 = HDFC("Piyus", 5000)  # __init__(100,"Piyush", 5000)
    obj2 = HDFC("Adi", 3000)  # __init__(100,"Adi", 3000)

    print("Perform operation on obj1")
    obj1.deposit(2000)
    obj1.DisBal()

    obj1.withDraw(1000)
    obj1.DisBal()

    print("Perform operation on obj2")
    obj2.deposit(4000)
    obj2.DisBal()

    obj2.withDraw(20000)
    obj2.DisBal()


if __name__ == "__main__":
    main()


----------------------------


import Module1
import Module2

def main():
    print("Special variable of starter.py is ", __name__)

    Module1.DisplayModule1()
    Module2.DisplayModule2()


if __name__ == "__main__":
    main()


-------------------------


def checkPrime(no) -> bool:
    count = int(no/2) + 1
    counter = 2
    while(counter == count):
        if(no % counter == 0):
            return True
        counter += 1
    return False


def acceptnumber():
    no = int(input("Enter nos of Elements: "))
    nos = []

    for i in range(0, no):
        nos.append(int(input(f"Enter the {i} element: ")))

    print(nos)

    primesTotal = 0
    for i in range(0, no):
        if(checkPrime(nos[i])):
            primesTotal += nos[i]

    print(primesTotal)


def main():
    acceptnumber()


if __name__ == "__main__":
    main()


---------------------------------------


class Demo:

    def __init__(self, val1, val2) -> None:    #constructor
        print("Inside Init Method")
        self.no1 = val1
        self.no2 = val2

    def display(self):
        print("Value of No1: ", self.no1)
        print("Value of No2: ", self.no2)


def main():
    print("Demostration of object orrientation")

    obj1 = Demo(10, 20)   #__init__(100, 10, 20)
    obj2 = Demo(10, 54)   #__init__(100, 10, 54)

    obj1.display()  #display(100)
    obj2.display()  #display(200)

if __name__ == "__main__":
    main()



-----------------------------

import os
import threading

def task1(value):
    print("PID of Task1 is: ", os.getpid())
    print("ThreadID of Task1 process: ", threading.get_ident())
    print("ThreadID of Task1 process: ", threading.current_thread())


def task2(value):
    print("PID of Task2 is: ", os.getpid())
    print("ThreadID of Task2 process: ", threading.get_ident())
    print("ThreadID of Task1 process: ", threading.current_thread())

def main():
    print("PID of parent process: ", os.getpid())
    print("ThreadID of parent process: ", threading.get_ident())
    print("ThreadID of Task1 process: ", threading.current_thread())


    no = 5
    t1 = threading.Thread(target = task1, args = (no, ))
    t2 = threading.Thread(target = task2, args = (no, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

















