def triangle():
    a = float(input("Enter the length of first side: "))

    b = float(input("Enter the length of second side: "))

    c = float(input("Enter the length of third side: "))

    if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):

        print("Triangle can be formed")

    else:

        print("Triangle can not be formed.")


def main():
    triangle()


if __name__ == "__main__":
    main()