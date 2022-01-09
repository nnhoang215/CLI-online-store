# FINAL Introduction to Programming assignment

# This project features an online store running on CLI. This online store sells books.

# an item should have the following attributes:
# {id, price, total_quantity, colors(quantity of each), weight, size, tech specs, reviews}

master_dictionary = {
    "Iphone 13 Pro Max": {
        "id": "1001",
        "price": 32000000,
        "total_quantity": 40,
        "colors": {
            "blue": 10,
            "green": 10,
            "purple": 10,
            "white": 10},
        "weight": "240 grams",
        "sizes": "6.7 inches",
        "tech specs": """
            IP68 Water Resistance,
            A15 Bionic chip
            New 6‑core CPU with 2 performance and 4 efficiency cores
            New 5‑core GPU
            New 16‑core Neural Engine
            Pro 12MP camera system: Telephoto, Wide, and Ultra Wide cameras
            Cinematic mode for recording videos with shallow depth of field (1080p at 30 fps)
            FaceID 
            22 hours of video playback with a single charge
            For more info, checkout the product's official website:https://www.apple.com/vn/iphone-13-pro/specs""",
        "reviews": {"likes": 0, "dislikes": 0}
    },
    "Iphone 13 Pro": {
        "id": "1002",
        "price": 32000000,
        "total_quantity": 40,
        "colors": {
            "blue": 10,
            "green": 10,
            "purple": 10,
            "white": 10},
        "weight": "200 grams",
        "sizes": "6.1 inches",
        "tech specs": """
            IP68 Water Resistance,
            A15 Bionic chip
            New 6‑core CPU with 2 performance and 4 efficiency cores
            New 5‑core GPU
            New 16‑core Neural Engine
            Pro 12MP camera system: Telephoto, Wide, and Ultra Wide cameras
            Cinematic mode for recording videos with shallow depth of field (1080p at 30 fps)
            FaceID
            22 hours of video playback with a single charge
            For more info, checkout the product's official website:https://www.apple.com/vn/iphone-13-pro/specs""",
        "reviews": {"likes": 0, "dislikes": 0}
    }
}
shopping_cart = {"items": [], "total_price": 0}

while True:
    display_list = []
    new_list = []


    def get_all_items():
        for j, k in master_dictionary.items():
            if j not in new_list:
                new_list.append(j)
            print(j)
        return new_list


    def get_items_details():
        for j, k in master_dictionary.items():
            print(j, k)


    def filter_by_name(search_input):
        for e in new_list:
            if search_input in e.replace(" ", "").lower():
                display_list.append(e)


    def filter_by_id(search_input):
        for e in new_list:
            if search_input in e["id"]:
                display_list.append(e)


    user_input = int(input("input a name: ").lower().replace(" ", ""))
    if user_input == "/stop":
        break
    else:
        get_all_items()
        print(new_list)
        # filter_by_name(user_input)
        filter_by_id(user_input)
        print(display_list)

#menu  
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

Menu()






#Menu V2
import sys
#1
def displayList():
    print()
    print("---AVAILABLE ITEMS---")
    for i in shopping_list:
        print ("*" + i )
#shopping cart


#2
def displayCart():
    print()
    print("---YOUR CART---")
    print(shopping_cart)

shopping_cart = []
#3
def addItem():
    item = input("Enter desired item: ")
    if item in shopping_list:
        print(item + " has been successfully added to your cart")
        shopping_cart.append(item)
    else:
        print(item + " is currently not in our shop")

    print(shopping_cart)

#4
def removeItem():
    item = input("Enter undesired item: ")
    if item in shopping_list:
        shopping_cart.remove(item)
        print(item + " has been successfully removed to your cart")
    else:
        print(item + " not found in your cart")
    print(shopping_cart)

#5
def checkItem():
    item = input("What item are you looking for?:")
    if item in shopping_list:
        print("The item you are looking for " + item + " is in the shop ")
        answer = input("Do you want to add " + item + " to your cart?: ")
        if answer == "Yes":
            print(item + " has successfully added to the cart!")
            shopping_cart.append(item)
            choice = input("Do you want to keep searching?:")
            while choice == "Yes":
                item = input("What item are you looking for?:")
                if item in shopping_list:
                    print("The item you are looking for " + item + " is in the shop ")
                    answer = input("Do you want to add " + item + " to your cart?: ")
                    if answer == "Yes":
                        print(item + " has successfully added to the cart!")
                        shopping_cart.append(item)
                        choice = input("Do you want to keep searching?: ")
                    else:
                        print("Thank you for checking our product")
                        choice = input("Do you want to keep searching?:")
                else:
                    print("The item you are looking for " + item + " currently not in our shop ")
                    choice = input("Do you want to keep searching?: ")

        else:
            print("Thank you for checking our product.")
            choice = input("Do you want to keep searching?: ")
            while choice == "Yes":
                item = input("What item are you looking for?:")
                if item in shopping_list:
                    print("The item you are looking for " + item + " is in the shop ")
                    answer = input("Do you want to add " + item + " to your cart?: ")
                    if answer == "Yes":
                        print(item + " has successfully added to the cart!")
                        shopping_cart.append(item)
                        choice = input("Do you want to keep searching?: ")
                    else:
                        print("Thank you for checking our product")
                        choice = input("Do you want to keep searching?:")
                else:
                    print("The item you are looking for " + item + " currently not in our shop ")
                    choice = input("Do you want to keep searching?: ")


    else:
        print("The item you are looking for " + item + " currently not in our shop ")
        choice = input("Do you want to keep searching?: ")
        while choice == "Yes":
            item = input("What item are you looking for?:")
            if item in shopping_list:
                print("The item you are looking for " + item + " is in the shop ")
                answer = input("Do you want to add " + item + " to your cart?: ")
                if answer == "Yes":
                    print(item + " has successfully added to the cart!")
                    shopping_cart.append(item)
                    choice = input("Do you want to keep searching?: ")
                else:
                    print("Thank you for checking our product")

            else:
                print("The item you are looking for " + item + " currently not in our shop ")
                choice = input("Do you want to keep searching?: ")


#6
def clearList():
    shopping_cart.clear()
    print("Your cart now is empty")


#shopping list
shopping_list = ["Iphone 13 Pro Max", "Iphone 13 Pro", "Nvidia RTX 3090", "Nike Dior 1", "apple","bread","cookie","milktea","hoodie","cake"]

def Menu():
    while True:
        print()
        print(''' ### SHOPPING LIST ### 
        ---SELECT A FEATURE YOU WOULD LIKE TO USE---:
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
            displayCart()
        elif selection == "3":
            addItem()
        elif selection == "4":
            removeItem()
        elif selection == "5":
            checkItem()
        elif selection == "6":
            pass
        elif selection == "7":
            clearList()
        elif selection == "8":
            print("Thank you for shopping at our store!")
            sys.exit()

        else:
            print("This feature is currently not available")

Menu()
