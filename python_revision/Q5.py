def wavelength():

    wl = int(input("Enter the wavelength in nm: "))

    if 380 <= wl < 450:

        print("Color : Violet")

    elif 450 <= wl < 495:

        print("Color : Blue")

    elif 495 <= wl < 570:

        print("Color : Green")

    elif 570 <= wl < 590:

        print("Color : Yellow")

    elif 590 <= wl < 620:

        print("Color : Orange")

    elif 620 <= wl <= 750:

        print("Color : Red")

    else:

        print("Please enter in the range between 380 to 750")

def main():

    wavelength()

if __name__ == "__main__":

    main()