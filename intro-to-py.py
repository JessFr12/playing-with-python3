# Input your first name, last name, age, and gender
first_name = input("First Name: ")
last_name = input("Last Name: ")
age = int(input("Age: "))
gender = input("M or F? ")
correct = True
# Create message to confirm information
if gender.lower == "m":
    print("Hello Mr." + last_name + "! Thank you for your info.\n"
        + first_name + "\n" + last_name + "\n" + str(age) + "\n" + gender)
else:
    print("Hello Ms." + last_name + "! Thank you for your info.\n"
        + first_name + "\n" + last_name + "\n" + str(age) + "\n" + gender)
