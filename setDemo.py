print("Demonstration of set")


set1 = {10, 'Hello', True, 4556.278528}
print(set1)

set2 = {10, 10, 745}
print(set2)

#set2[1] = 68
#print(set2[1])

set2.add(51)
print(set2)

set2.remove(10)
print(set2)

for val in set1:
    print(val)

no = int(input('Enter no to find: '))

for val in set1:
    if(no == val):
        print('found')
