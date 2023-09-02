class BookStore:

    noOfBooks = 0

    def __init__(self, name, author):
        self.name = name
        self.author = author
        BookStore.noOfBooks += 1

    def Display(self):
        print(self.name + self.author + str(BookStore.noOfBooks))


def main():
    obj1 = BookStore("LSP", "RObert")
    obj2 = BookStore("ABC", "Chort")

    obj1.Display()
    obj2.Display()


if __name__ == '__main__':
    main()
