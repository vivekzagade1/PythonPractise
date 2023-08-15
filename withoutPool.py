def square(no):
    return no*no

def main():
    arr = [10, 20, 30, 40, 50]
    res = []

    for val in arr:
        ans = square(val)
        res.append(ans)

    print(res)

if __name__ == "__main__":
    main() 