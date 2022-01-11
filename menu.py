import sys

def displayList():
    print()
    print("---AVAILABLE ITEMS---")
    for i in shopping_list:
        print ("*" + i )
#shopping cart
shopping_cart = []

def displayCart():
    print()
    print("---YOUR CART---")
    print(shopping_cart)

def addItem():
    item = input("Enter desired item: ")
    shopping_cart.append(item)
    print(item + " has been successfully added to your cart")
    print(shopping_cart)


def removeItem():
    item = input("Enter undesired item: ")
    shopping_cart.remove(item)
    print(item + " has been successfully added to your cart")
    print(shopping_cart)

#shopping list
shopping_list = ["Iphone 13 Pro Max", "Iphone 13 Pro", "Nvidia RTX 3090", "Nike Dior 1"]

def Menu():
    while True:
        print()
        print(''' ### SHOPPING LIST ### 
        SELECT A NUMBER YOU WOULD LIKE TO CHOOSE:
        1. View shopping list
        2. View shopping cart 
        3. Add item to shopping cart
        4. Remove item from shopping cart 
        5. Search item by name
        6. Search item by id
        7. Clear shopping cart
        8. End shopping 
        ''')

        selection = input("What do you want to do: ")
        if selection == "1":
            displayList()
        elif selection == "2":
            displayCart
        elif selection == "3":
            addItem()
        elif selection == "4":
            removeItem()
        elif selection == "5":
            pass
        elif selection == "6":
            pass
        elif selection == "7":
            sys.exit()
        else:
            print("This feature is currently not available")

# Menu()
