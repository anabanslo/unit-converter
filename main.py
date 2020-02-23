print("Greetings visitor! This is a unit converter.")
while True:
    km = input("Kilometers: ")

    km = float(km.replace(",", "."))  # replace comma with dot, if user entered a comma

    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break