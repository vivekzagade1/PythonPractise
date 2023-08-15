books = {
    'ppa': 'a',
    'python': 'b',
    'angular': 'c'
}

print(books)
print(type(books))
print(len(books))
print(books['ppa'])

for val in books:
    print(val)

for val in books:
    print(books[val])

for val in books:
    print(val, books[val])

batch = books.keys()
print(type(batch))

values = books.values()
print(type(values))