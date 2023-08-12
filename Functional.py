def Display(Name, Age=54):
    print(Name)
    print(Age)


def main():
    Display("Sagar", 27)
    Display(Name="Vishal", Age=45)
    Display(Age=65, Name="Hrishi")
    Display("Nilesh")


if __name__ == "__main__":
    main()