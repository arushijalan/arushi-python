def arithmetic():

    a = float(input("Enter the first number: "))

    b = float(input("Enter the second number: "))

    sum = a+b

    print(f"The sum of {a} and {b} is", sum)

    product = a*b

    print(f"The product of {a} and {b} is", product)

    difference = a-b

    print(f"The difference of {a} and {b} is", difference)

    quotient = a/b

    print(f"The quotient of {a} divided by {b} is", quotient)

    remainder = a%b

    print(f"The remainder of {a} divided by {b} is", remainder)

def main():

    arithmetic()

if __name__ == "__main__":

    main()