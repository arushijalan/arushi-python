def prime():
    num = int(input("Enter a number: "))

    if num < 2:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True


def main():
    if prime():

        print("Prime number")

    else:

        print("Composite number")


if __name__ == "__main__":
    main()