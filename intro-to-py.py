# Input your first name, last name, age, and gender
# Create message to confirm information
try:
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    gender = input("M or F? ")
    correct = True
    # Still need to insert conditions for error handling
    # Gender should only contain M or F
    # Age should not be < 0 or > 100
    # Name should only accept letters
    if not first_name.isalpha():
        raise ValueError()
    if not last_name.isalpha():
        raise ValueError()
    if not age > 0:
        print("That is not quite possible. (Age must be over 0 and under 100)")
        raise ValueError()
    if not age < 100:
        print("That is not quite possible. (Age must be over 0 and under 100)")
        raise ValueError()
    
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