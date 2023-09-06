# Input your first name, last name, age, and gender
# Create message to confirm information
try:
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    gender = input("M or F? ")
    correct = True
    if gender == "m" or gender == "M":
        print("Hello Mr." + last_name + "! Thank you for your info.\n"
            + first_name + "\n" + last_name + "\n" + str(age) + "\n" + gender)
    else:
        print("Hello Ms." + last_name + "! Thank you for your info.\n"
            + first_name + "\n" + last_name + "\n" + str(age) + "\n" + gender)
except:
    print("Name must contain only letters, age must be only integers, "
          + "and gender should only contain characters (M or F)")
finally:
    print("Please try again as you please!")