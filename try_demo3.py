
def main():
    try:
        print('Enter first number: ')
        no1 = int(input())

        print('Enter first number: ')
        no2 = int(input())

        ans = no1 / no2

    except ZeroDivisionError as e:
        print(f'Zero division error by {e}')
        return

    except ValueError as e:
        print(f'{e}')
        return

    except Exception as e:
        print(f'{e}')
        return

    print(f"Div is {ans}")


if __name__ == '__main__':
    main()
