def comma():
    two_words = input("Please enter two words separated with a comma: ")

    two_words = two_words.replace(",", " and ")

    print(two_words)


def main():
    comma()


if __name__ == "__main__":
    main()

