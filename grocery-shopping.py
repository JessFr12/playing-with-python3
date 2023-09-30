# In this practice I want to create a mini store
# with a couple of priced items that customers are able
# to choose from

print("Hello! Welcome to our Market, how are you doing? ")
input()
print("Well we are so happy that you are here!\n"
      + "Please take a look at our selection and let us know if you " 
      + "need any help.\n")

food = {
    "Milk": 3.29, "Apple juice": 2.99, "Bananas": 3.00, "Bread": 2.50,
      "Potato Chips": 1.50, "Cookies": 2.40, "Beef": 4.00
}
def print_menu():
    for key, value in food.items():
        print(f"{key}: {value}")
print_menu()