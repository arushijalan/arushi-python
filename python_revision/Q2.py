def pythagoras():
    a = float(input("Enter the length of first short side of right angled triangle: "))

    b = float(input("Enter the length of second short side of right angled triangle: "))

    c = float(((a ** 2) + (b ** 2)) ** 0.5)

    print("The length of hypotaneous is", c)


def main():
    pythagoras()


if __name__ == "__main__":
    main()

