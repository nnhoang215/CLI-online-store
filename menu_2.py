import json
import common
import sys
import re

#1
def get_shopping_list():
    shopping_list = []
    with open("products.json") as json_file:
        data = json.load(json_file)
    for item in data["products"]:
        product = []
        product.extend((item["name"], item["price"], item["quantity"]))
        shopping_list.append(product)
    return shopping_list

shopping_list = get_shopping_list() # [['Iphone 13 Pro Max Pink', 100, 40], ['Iphone 13 Blue', 200, 20], ['JBL Pulse 3', 200, 40], ['JBL Pulse 4', 300, 40]]

def displayList():
    with open("products.json") as json_file:
        data = json.load(json_file)
    common.print_highlight("---AVAILABLE ITEMS---")
    for i in range(len(shopping_list)):
        item = shopping_list[i]
        common.print_highlight("*" + str(i) + " " + str(item[0]) + " - " + str(item[1]) + "$ - " + str(item[2]) + " left")
  
    # for product in data["products"]:
    #     common.print_highlight("*" + str(product["name"]) + " " + str(product["price"]) + "$")
    # print()
    # 
    # for i in shopping_list:
    #     print ("*" + i )
#shopping cart


#2
def displayCart():
    print()
    print("---YOUR CART---")
    common.print_highlight(str(SHOPPING_CART))

SHOPPING_CART = []
#3
def addItem():
    item_index = int(common.input_highlight("Enter desired item index : "))
    item_quantity = int(common.input_highlight("Quantity : "))
    try: 
        item = shopping_list[item_index]
        item.append(item_index) 
        item[2] = item_quantity
        if item and (item[2] != 0):
            SHOPPING_CART.append(item)
            common.print_success("Successfully added! Your cart: " + str(SHOPPING_CART))
    except:
        common.print_fail("Item not available")
    # item = input("Enter desired item: ")
    # if item in shopping_list:
    #     print(item + " has been successfully added to your cart")
    #     SHOPPING_CART.append(item)
    # else:
    #     print(item + " is currently not in our shop")

    # print(SHOPPING_CART)

#4
def removeItem():
    item_index = int(input("Enter undesired item index: "))

    try:
        item = SHOPPING_CART[item_index]
        if item:
            SHOPPING_CART.pop(item_index)
            common.print_success("Removed " + str(item[0]) + "." + "\n" + "Your cart: " + str(SHOPPING_CART))
    except:
        common.print_fail("Item not in your cart!")
    # if item in shopping_list:
    #     SHOPPING_CART.remove(item)
    #     print(item + " has been successfully removed to your cart")
    # else:
    #     print(item + " not found in your cart")
    # print(SHOPPING_CART)

#5
with open("products.json") as json_file:
    data = json.load(json_file)
    lst_products = data["products"]
    
# filter items by name
def filter_by_name():
    # This function takes string as an input to spot the string input in the products list
    # It will return a list of products that have the word written in the string

    search_input = input("Please enter the name of the item you want to find: \n>")
    item_list = []
    for i in range(0, len(lst_products)):
        match_keyword = re.findall(search_input, lst_products[i].get('name'))
        if match_keyword:
            item_list.append(lst_products[i].get('name'))
        else:
            pass
    print("Here is the result of your search:")
    if not item_list:
        print("None")
    else:
        for num in range(0, len(item_list)):
            print('{}.'.format(num+1) + item_list[num])

#6
# filter items by id
def filter_by_id():
    # This function takes string as an input to spot the string input in the products list
    # It will return a list of products containing the id

    search_input = input("Please enter the id of the item you want to find: \n>")
    item_list = []
    for i in range(0, len(lst_products)):
        match_keyword = re.findall(search_input, lst_products[i].get('id'))
        if match_keyword:
            word_added = "[{}] {}".format(lst_products[i].get('id'), lst_products[i].get('name'))
            item_list.append(word_added)
        else:
            pass
    print("Here is the result of your search:")
    if not item_list:
        print("None")
    else:
        for num in range(0, len(item_list)):
            print('{}. {}'.format(num+1, item_list[num]))

#7
def clearList():
    SHOPPING_CART.clear()
    common.print_success("Your cart now is empty.")

#8
def purchase():
    
    # for i in range(len(shopping_list)):
        # item = shopping_list[i]
    for j in range(len(SHOPPING_CART)):
        cart_item = SHOPPING_CART[j]
        shopping_list_index = cart_item[3]
        # print(shopping_list_index)
        shopping_list[shopping_list_index][2] = int(shopping_list[shopping_list_index][2]) - int(cart_item[2])
    print(shopping_list)
        # item[2] - SHOPPING_CART[]
#9


#shopping list
# shopping_list = ["Iphone 13 Pro Max", "Iphone 13 Pro", "Nvidia RTX 3090", "Nike Dior 1", "apple","bread","cookie","milktea","hoodie","cake"]

def menu_2():
    while True:
        print()
        common.print_highlight(''' ### SHOPPING LIST ### 
        ---SELECT A FEATURE YOU WOULD LIKE TO USE---:
        1. View shopping list                               6. Search item by id
        2. View shopping cart                               7. Clear shopping cart
        3. Add item to shopping cart                        8. Purchase
        4. Remove item from shopping cart                   9. Exit shop
        5. Search item by name                             
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
            filter_by_name()
        elif selection == "6":
            filter_by_id()
        elif selection == "7":
            clearList()
        elif selection == "8":
            pass
        elif selection == "9":
            print("Thank you for shopping at our store!")
            sys.exit()
        else:
            print("This feature is currently not available")


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
            SHOPPING_CART.append(item)
            choice = input("Do you want to keep searching?:")
            while choice == "Yes":
                item = input("What item are you looking for?:")
                if item in temp_list:
                    print("The item you are looking for " + item + " is in the shop ")
                    answer = input("Do you want to add " + item + " to your cart?: ")
                    if answer == "Yes":
                        print(item + " has successfully added to the cart!")
                        SHOPPING_CART.append(item)
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
                        SHOPPING_CART.append(item)
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
                    SHOPPING_CART.append(item)
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
            SHOPPING_CART.append(item)
            choice = input("Do you want to keep searching?:")
            while choice == "Yes":
                item = input("What item are you looking for?:")
                if item in temp_list:
                    print("The item you are looking for " + item + " is in the shop ")
                    answer = input("Do you want to add " + item + " to your cart?: ")
                    if answer == "Yes":
                        print(item + " has successfully added to the cart!")
                        SHOPPING_CART.append(item)
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
                        SHOPPING_CART.append(item)
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
                    SHOPPING_CART.append(item)
                    choice = input("Do you want to keep searching?: ")
                else:
                    print("Thank you for checking our product")

            else:
                print("The item you are looking for " + item + " currently not in our shop ")
                choice = input("Do you want to keep searching?: ")

