import json
import re


def write_json(data, file_name="products.json"):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)


with open("products.json") as json_file:
    data = json.load(json_file)
    lst_products = data["products"]


# filter items by name
def filter_by_name():
    # This function takes string as an input to spot the string input in the products list
    # It will return a list of products that have the word written in the string
    stopword = 'y'
    while stopword == 'y':
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
        while True:
            stopword = input("Do you want to continue searching? [y/n] \n>")
            if stopword in ['y','n']:
                break


# filter items by id
def filter_by_id():
    # This function takes string as an input to spot the string input in the products list
    # It will return a list of products containing the id
    stopword = 'y'
    while stopword == 'y':
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
        while True:
            stopword = input("Do you want to continue searching? [y/n] \n>")
            if stopword in ['y','n']:
                break

