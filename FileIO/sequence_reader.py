import sys


def read_series(filename):
    """ f = open(filename, mode='rt', encoding='utf-8')
    series = []
    try:
        for line in f:
            a = int(line.strip())
            series.append(a)
    finally:
        f.close()
    return series"""
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main(filename=sys.argv[1])
