def cylinder_volume():

    r = float(input("Enter the radius of the base: "))

    h = float(input("Enter the height of the cylinder: "))

    volume = float(3.14*(r**2)*h)

    print("The volume of the cynlider is", volume)

def main():

    cylinder_volume()

if __name__ == "__main__" :

    main()

