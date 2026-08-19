age = int(input("Enter your age: "))
passport = input("Do you have a passport? ")

if age >= 18:
    if passport.lower() == "yes":
        print("You can go on a trip to America.")
    else:
        print("You can travel within your country.")
else:
    print("You are not eligible.")