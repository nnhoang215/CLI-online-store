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
    },
    "Nvidia RTX 3090": {
        "id": "1003",
        "price": 69999000,
        "total_quantity": 1,
        "weight": "219 grams",
        "sizes": "12.3 inches",
        "tech specs": """
            NVIDIA CUDA Cores 10496
            NVIDIA CUDA Cores 10496
            Boost Clock	1.70 GHz
            Memory Size	24 GB
            Memory Type	GDDR6X
            For more info, checkout the product's official website:https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/""",
        "reviews": {"likes": 0, "dislikes": 0}
    },
    "Nike Dior 1": {
        "id": "1004",
        "price": 533863467,
        "total_quantity": 1,
        "weight": "2400 grams",
        "sizes": "11 inches",
        "tech specs": """
            Release Fall 2020
            Only 8000 pairs were made
            A collaboration between Nike and Dior 
            For more info, checkout the product's official website: https://stockx.com/air-jordan-1-retro-high-dior""",
        "reviews": {"likes": 0, "dislikes": 0}
    },
    "
    

    
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


   def filter_by_name():
        search_input = input("Please enter the name of the item you want to find: \n>")
        temp_list = []
        for j in master_dictionary.keys():
            temp_list.append(j)
        if search_input in temp_list:
            quantity = master_dictionary.get(search_input).get("total_quantity")
            print("There are {} {} available at our store.".format(quantity, search_input))
        else:
            print("We're very sorry but our shop does not provide that item.")


    def filter_by_id():
        search_input = str(input("Please enter the id of the item you want to find: \n>"))
        temp_list = []
        for i in master_dictionary.values():
            temp_list.append(i.get('id'))
        if search_input in temp_list:
            for key, val in master_dictionary.items():
                if search_input == master_dictionary.get(key).get("id"):
                    quantity = master_dictionary.get(key).get("total_quantity")
                    print("The id belongs to {}, and there are {} of them in our store.".format(key, quantity))
                else:
                    pass
        else:
            print("There is no id like that in our shop.")


    user_input = input("input a name: ").lower().replace(" ", "")
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
        for j in master_dictionary:
        print("* " + j)
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



#find by name
def checkItem():
    item = input("Please enter the name of the item you want to find: \n")
    temp_list = []
    for item in master_dictionary.keys():
        temp_list.append(item)
    if item in temp_list:
        print("The item you are looking for" + item + " is in the shop")
        answer = input("Do you want to add " + item + " to your cart?: ")
        if answer == "Yes":
            print(item + " has successfully added to the cart!")
            shopping_cart.append(item)
            choice = input("Do you want to keep searching?:")
            while choice == "Yes":
                item = input("What item are you looking for?:")
                if item in temp_list:
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
            print("We're very sorry but our shop does not provide that item.")
            choice = input("Do you want to keep searching?: ")
            while choice == "Yes":
                item = input("What item are you looking for?:")
                if item in temp_list:
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
            if item in temp_list:
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
                
                
                
                
                
                
   #search by name and feature
def checkItem():
    item = input("Please enter the name of the item you want to find: \n")
    temp_list = []
    for j in master_dictionary.keys():
        temp_list.append(j)
    if item in temp_list:
        print("The item you are looking for " + item + " is in the shop")
        answer = input("Do you want to add " + item + " to your cart?: ")
        if answer == "Yes":
            print(item + " has successfully added to the cart!")
            shopping_cart.append(item)
            choice = input("Do you want to keep searching?:")
            while choice == "Yes":
                item = input("What item are you looking for?:")
                if item in temp_list:
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
                if item in temp_list:
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
            if item in temp_list:
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

