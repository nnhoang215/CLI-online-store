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
        item = shopping_list[item_index].copy()
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
    common.print_function("Search item by name")
    stop_word = "y"
    while stop_word == 'y':
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
            common.print_fail("None")
        else:
            for num in range(0, len(item_list)):
                common.print_success('{}.'.format(num+1) + item_list[num])

        while True:
            stop_word = input("Would you like to continue searching? [y/n] \n>")
            if stop_word in ['y', 'n']:
                break

#6
# filter items by id
def filter_by_id():
    # This function takes string as an input to spot the string input in the products list
    # It will return a list of products containing the id
    common.print_function("Search item by name")
    stop_word = "y"
    while stop_word == 'y':
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
            common.print_fail("None")
        else:
            for num in range(0, len(item_list)):
                common.print_success('{}. {}'.format(num+1, item_list[num]))
        while True:
            stop_word = input("Would you like to continue searching? [y/n] \n>")
            if stop_word in ['y', 'n']:
                break



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
service_lst = [
    {'name': "Standard service",
     'price': 50,
     'description': """
---SERVICE'S DESCRIPTION---
1. Scheduled shipping time with the customer
(Delivery takes at least 2 days)
2. Standard wrapping material
3. Include: 
    - a rose
    - a gifting card hand-written by our staff
---------------------------
     """
    },
    {'name': 'Premium service',
     'price': 200,
     'description': """
---SERVICE'S DESCRIPTION---
1. Scheduled shipping time with the customer
(Delivery takes at least 2 days)
2. Premium wrapping material
(Will schedule meeting with customer to take custom wrapping order)
3. Include: 
    - a flower bouquet 
    - balloons
    - a teddy bear
    - a gifting card hand-written by our staff and sealed with our shop wax seal  
---------------------------
     """
    }
]
def print_message():
    print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')


def choose_service():
    print("Okay. Here are two gifting services that we are currently providing:")
    for i in range(0,len(service_lst)):
        print(service_lst[i].get('description'))
    gift_service = input("Please choose your option: \n[a] Standard \n[b] Premium \n>")
    if gift_service == 'a':
    # return tiền để tí cộng vào bill checkout
        return 50
    elif gift_service == 'b':
        return 100
    else:
        print_message()
        return choose_service()

def notify_email():
    send_email = input("Do you want to send an email notifying the recipient? [y/n] \n>")
    if send_email == 'y':
        pass # để tạm :))
        # Gửi mail vs nội dung là "You have received a gift from ..."
    elif send_email == 'n':
        print("Sure")
        pass
    else:
        print_message()
        return notify_email()


def gift_item():
    # This function take email of the person that receive the gift of the user to print out the recipient's address
    # It will also offer deals and services when gifting someone
    # return the price of the chosen service
    user_input = input("Please enter the email of the gift recipient: \n>")
    print("The gift will be delivered to {}".format(get_address(user_input)))
    bill_service = choose_service()
    notify_email()
    # return price of service rồi lúc viết
    # chỉ cần khai thêm biến = gift_item() rồi cộng vào để check out
    return bill_service



#shopping list
# shopping_list = ["Iphone 13 Pro Max", "Iphone 13 Pro", "Nvidia RTX 3090", "Nike Dior 1", "apple","bread","cookie","milktea","hoodie","cake"]

#11 get_info from auth.py
    
def menu_2():
    while True:
        print()
        common.print_highlight(''' ### SHOPPING LIST ### 
        ---SELECT A FEATURE YOU WOULD LIKE TO USE---:
        1. View shopping list                               6. Search item by id                        11. Get user info
        2. View shopping cart                               7. Clear shopping cart
        3. Add item to shopping cart                        8. Purchase
        4. Remove item from shopping cart                   9. Gifting service
        5. Search item by name                              10. Exit shop
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
            gift_item()
        elif selection == "10":
            print("Thank you for shopping at our store!")
            sys.exit()
        elif selection == "11":
            get_info(IS_ADMIN, CURRENT_USER)
        else:
            print("This feature is currently not available")




                
# #
# products_string ='''
# {
#     "products": [
#         {
#             "name": "Iphone 13 Pro Max Pink",
#             "category": "Phone",
#             "id": "1001",
#             "quantity": 40,
#             "color": "Pink",
#             "weight": "240g",
#             "size": "6.7in",
#             "tech_specs": "IP68 Water Resistance, A15 Bionic chip, For more info, checkout the product's official website:https://www.apple.com/vn/iphone-13-pro/specs",
#             "reviews": {"likes": 0, "dislikes": 0}
#         },
#         {
#             "name": "Iphone 13 Blue",
#             "category": "Phone",
#             "id": "1002",
#             "quantity": 20,
#             "color": "Blue",
#             "weight": "240g",
#             "size": "6.7in",
#             "tech_specs": "IP68 Water Resistance, A15 Bionic chip, For more info, checkout the product's official website:https://www.apple.com/vn/iphone-13-pro/specs",
#             "reviews": {"likes": 0, "dislikes": 0}
#         },
#         {
#             "name": "JBL Pulse 3",
#             "category": "Audio",
#             "id": "1003",
#             "quantity": 40,
#             "color": "Green",
#             "weight": "103g",
#             "size": "10in",
#             "tech_specs": "add them vao nhe",
#             "reviews": {"likes": 0, "dislikes": 0}
#         },
#         {
#             "name": "JBL Pulse 4",
#             "category": "Audio",
#             "id": "1004",
#             "quantity": 40,
#             "color": "Yellow",
#             "weight": "240g",
#             "size": "6.7in",
#             "tech_specs": "add them vao",
#             "reviews": {"likes": 0, "dislikes": 0}
#         }
#     ]
# }
# '''

# items = json.loads(products_string)['products']load the json data
# def checkAll():
#     search_text = input("Enter an item name:\n")# Input the item name that you want to search

#     result = 0
#     for i in range(len(items)):
#         if search_text.lower() in items[i]["name"].lower():
#             result = result + 1
#             print("-------------------------")
#             print("Product name: ", items[i]["name"])
#             print("Product category: ", items[i]["category"])
#             print("Product quantity: ", items[i]["quantity"])
#             print("Product color: ", items[i]["color"])
#             print("Product size: ", items[i]["category"])
#             print("Product specs: ", item[i]["tech_specs"])

#     if result == 0:
#         print("No result")
