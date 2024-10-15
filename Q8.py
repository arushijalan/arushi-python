def article():

    word = input("Enter a word: ")

    if word[0] in "aeiou":

        print(f"An {word}")

    else:

        print(f"A {word}")

def main():

    article()

if __name__ == "__main__":

    main()