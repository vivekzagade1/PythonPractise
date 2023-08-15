batches = {
    'ppa': 12121,
    'python': 851,
    'angular': 8454
}

print(batches)
print(type(batches))
print(len(batches))
print(batches['ppa'])

for val in batches:
    print(val)

for val in batches:
    print(batches[val])

for val in batches:
    print(val, batches[val])