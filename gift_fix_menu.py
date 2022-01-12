import pandas as pd
from pandas.core.algorithms import isin
from pandas.core.indexes.base import Index
from confirmation import send_signup_confirmation
import common
import json
import common
import sys
import re

users = pd.read_csv('users.csv')

CURRENT_USER = users.iloc[0]
IS_LOGGED_IN = False
IS_ADMIN = False

#full_name,email,key,address,phone number,items bought,total expense 
def get_address(email):
    user = users[(users['email'] == email)]
    user_index = user.index[0]
    address = users.at[user_index, 'address']
    return address

def sign_up():
    users = pd.read_csv('users.csv')
    common.print_function("Signing up for new user")

    signup_email = input("Your email address(used to sign in):")
    is_email_available = users[(users['email'] == signup_email)].empty
    
    if is_email_available:
        signup_key = str(input("Enter a password: "))
        confirm_key = input("Re-enter your password: ")

        if (signup_key == confirm_key):
            full_name = input("\t" + "What is your full name? ")
            address = str(input("\t" + "What is your address? "))
            phone = str(input("\t" + "What is your phone number? "))
        else:
            common.print_fail("Passwords do not match. Try again! \n")
            sign_up()

        new_user = pd.DataFrame({
            'full_name': [full_name],
            'email': [signup_email],
            'key': [signup_key],
            'address': [address],
            'phone_number': [phone],
            'items_bought': [0],
            'total_expense': [0],
        })
        new_user.to_csv('users.csv', mode = 'a', header = False, index=False)
        send_signup_confirmation(signup_email, signup_key, full_name)
        common.print_success("Let's sign in \n")
        sign_in()
    else:
        common.print_highlight("This email is already associated with an account \n")
        sign_in()
        
def sign_in():
    users = pd.read_csv('users.csv')
    common.print_function("Logging into your account")

    login_email = input("Email: ")

    user = users[(users['email'] == login_email)]
    if user.empty:
        common.print_fail("Wrong email. Please try again")
        choice = common.input_highlight("Enter '1' or '2'. [1] Try again | [2] Sign Up ")
        if choice == '1':
            sign_in()
        elif choice == '2':
            sign_up()
    else:
        user_index = user.index[0]

    login_key = str(input("Password: "))
    
    global IS_LOGGED_IN
    IS_LOGGED_IN = login_key == str(users.at[user_index, 'key'])

    if login_email == "admin":
        global IS_ADMIN
        IS_ADMIN = True

    if IS_LOGGED_IN:
        global CURRENT_USER
        CURRENT_USER = user
        print(CURRENT_USER)
        common.print_success("Login successfully \n")
    else:
        common.print_fail("Wrong password. Please try again")
        choice = common.input_highlight("Enter '1' or '2'. [1] Try again | [2] Sign Up ")
        if choice == '1':
            sign_in()
        elif choice == '2':
            sign_up()

def authenticate():
    choice = common.input_highlight("Enter '1' or '2'. [1] Sign Up | [2] Log In ")
    
    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    else:
        authenticate()




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
            match_keyword = re.findall(search_input, lst_products[i].get('name').lower())
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
    purchased_items = SHOPPING_CART.copy()
    total_cost = 0
    gift_service = input("Is this a gift for somebody? [y/n] \n>")
    if gift_service == 'y':
        total_cost += gift_item()
    elif gift_service == 'n':
        pass
    else:
        print_message()
        return purchase()
    for j in range(len(SHOPPING_CART)):
        cart_item = SHOPPING_CART[j]
        total_cost += (cart_item[1]*cart_item[2])
        shopping_list_index = cart_item[3]
        shopping_list[shopping_list_index][2] = int(shopping_list[shopping_list_index][2]) - int(cart_item[2])
    update_quantity(shopping_list)
    # order_confirmation()
    common.print_success("Successfully purchased " + str(SHOPPING_CART) + ". Total cost is " + str(total_cost)+ " dollars")
    clearList()

def update_quantity(shopping_list):
    json_file = open("products.json", "r")
    data = json.load(json_file)
    for i in range(len(shopping_list)):
        data["products"][i]["quantity"] = shopping_list[i][2] 
    json_file.close()

    json_file = open("products.json", "w")
    json.dump(data, json_file, indent=4)
    json_file.close()
        
        
#8.5
service_lst = [
    {'name': "Standard service",
     'description': """
---SERVICE'S DESCRIPTION---
Price: 50$
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
     'description': """
---SERVICE'S DESCRIPTION---
Price: 200$
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
        return 200
    else:
        print_message()
        return choose_service()

def notify_email():
    send_email = input("Do you want to send an email notifying the recipient? [y/n] \n>")
    if send_email == 'y':
        print("Okay, we will send a notification to the given email address.")
        common.print_success("Proceeding to check out...")
        pass # để tạm :))
        # Gửi mail vs nội dung là "You have received a gift from ..."
    elif send_email == 'n':
        print("Sure")
        common.print_success("Proceeding to check out...")
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

#10
# def exit_shop():


    
def menu_2():
    while True:
        print()
        common.print_highlight(''' ### SHOPPING LIST ### 
        ---SELECT A FEATURE YOU WOULD LIKE TO USE---:
        1. View shopping list                               6. Search item by id                        
        2. View shopping cart                               7. Clear shopping cart
        3. Add item to shopping cart                        8. Purchase
        4. Remove item from shopping cart                   9. Get user info
        5. Search item by name                             10. Exit shop
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
            purchase()
        elif selection == "9":
            common.print_success(get_info(IS_ADMIN, CURRENT_USER))
        elif selection == "10":
            print("Thank you for shopping at our store!")
            sys.exit()
        else:
            print("This feature is currently not available")


# #
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

def get_info(is_admin, current_user):
    users = pd.read_csv('users.csv')

    target_email = common.input_highlight("Email of who you want to search: ")
    target_user =  users[(users['email'] == target_email)]
    if is_admin:
        return target_user
    else:
        common.print_fail("\n You are not authorized to see other's information!")
        return current_user

def get_shopping_info(is_admin, current_user):
    users = pd.read_csv('users.csv')



def main():
    exit_program = False
    # authenticate()
    # while exit_program == False:
    menu_2()
    # print(get_shopping_list())
    # print(get_info(IS_ADMIN, CURRENT_USER))

main()

    
