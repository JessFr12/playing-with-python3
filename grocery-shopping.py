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
# list to store user's selection/s
user_selection = []
# Keep prompting the user for input until they are finished
while True:
    user_input = input("\nEnter an item (type 'done' when finished):\n")

    if user_input == "done": 
        break

    price = food.get(user_input, None)

    if price is None:
        print("Item is not available in store.")
        continue

    user_selection.append(user_input)


