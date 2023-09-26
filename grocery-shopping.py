# In this practice I want to create a mini store
# with a couple of priced items that customers are able
# to choose from

print("Hello! Welcome to our Market, how are you doing? ")
input()
print("Well we are so happy that you are here!\n"
      + "Please take a look at our selection and let us know if you " 
      + "need any help.\n")

food = ["Milk", "Apple juice", "Bananas", "Bread", "Potato Chips", "Cookies", "Beef"]
def print_menu():
    for menu in food:
        print(menu)
print_menu()