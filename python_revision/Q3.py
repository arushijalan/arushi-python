def median_of_3():

    n1 = int(input("Enter first number: "))

    n2 = int(input("Enter second number: "))

    n3 = int(input("Enter third number: "))

    list = [n1, n2, n3]

    list = sorted(list)

    median = list[1]

    print("The median is", median)

def main():

    median_of_3()

if __name__ == "__main__":

    main()