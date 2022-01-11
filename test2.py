import sys

master_dictionary = [{"id": 1001, "Name": "Iphone 13 Pro Max", "Available": 100, "Price": 32000000, "Type": "Tech"},
                     {"id": 1002, "Name": "IPhone 13 Pro", "Available": 100, "Price": 32000000, "Type": "Tech"},
                     {"id": 1003, "Name": "Nvidia RTX 3090", "Available": 10, "Price": 69999000, "Type": "Tech"},
                     {"id": 1004, "Name": "Nike Dior 1", "Available": 10, "Price": 533863467, "Type": "Shoes"},
                     {"id": 1005, "Name": "1963 Ferrari GTO", "Available": 10, "Price": 1179880000000, "Type": "Car"},
                     {"id": 1006, "Name": "The Card Players' ", "Available": 10, "Price": 6239750000000,
                      "Type": "Painting"},
                     {"id": 1007, "Name": "The Perfect Pink", "Available": 10, "Price": 521870000000,
                      "Type": "Jewelry"},
                     {"id": 1008, "Name": "Feather of Huia Bird", "Available": 100, "Price": 226900000,
                      "Type": "Decoration"},
                     {"id": 1009, "Name": "Diamond Panther Bracelet", "Available": 30, "Price": 281356000000,
                      "Type": "Jewelry"},
                     {"id": 1010, "Name": "Gold-plated Bugatti Veyron", "Available": 50, "Price": 226900000000,
                      "Type": "Car"},
                     {"id": 1011, "Name": "Dead Shark", "Available": 3, "Price": 272280000000, "Type": "Painting"},
                     {"id": 1012, "Name": "Magnetic floating bed", "Available": 1000, "Price": 36304000000,
                      "Type": "Furniture"},
                     {"id": 1013, "Name": "Crystal Piano", "Available": 50, "Price": 72608000000, "Type": "Decoration"},
                     {"id": 1014, "Name": "Saffron", "Available": 2000, "Price": 249590, "Type": "Material"},
                     {"id": 1015, "Name": "iPhone 3GS Supreme Rose", "Available": 20, "Price": 65801000000,
                      "Type": "Tech"},
                     {"id": 1016, "Name": "L’Incomparable Diamond Necklace", "Available": 70, "Price": 1247950000000,
                      "Type": "Jewelry"},
                     {"id": 1017, "Name": "201-cart gemstone watch", "Available": 40, "Price": 567250000000,
                      "Type": "Jewelry"},
                     {"id": 1018, "Name": "Graff Diamonds Hallucination Watch", "Available": 50, "Price": 1247950000000,
                      "Type": "Jewelry"},
                     {"id": 1019, "Name": "Limited Patek Philippe Watch", "Available": 20, "Price": 589940000000,
                      "Type": "Jewelry"},
                     {"id": 1020, "Name": "Tesla Model S", "Available": 100, "Price": 3403500000, "Type": "Car"}]


# 1
def displayAll():
    print()
    print("---AVAILABLE ITEMS---")
    print("Id\tName\tAvailable\tPrice\tOriginal Price")
    print("====================================================")
    for d in master_dictionary:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}\t{d["Type"]}')


# 2
def displayName():
    print()
    print("---AVAILABLE ITEMS---")
    print("Name")
    print("====================================================")
    for d in master_dictionary:
        print("*" + d["Name"])


def Menu():
    while True:
        print()
        print(''' ### SHOPPING LIST ### 
        SELECT A NUMBER YOU WOULD LIKE TO CHOOSE:
        1. View shopping list
        2. View available items
        3. Add item to shopping cart
        4. Remove item from shopping cart 
        5. Search item by name
        6. Search item by id
        7. Clear shopping cart
        8. End shopping 
        ''')

        selection = input("What do you want to do: ")
        if selection == "1":
            displayAll()
        elif selection == "2":
            displayName()
        elif selection == "3":
            pass
            ()
        elif selection == "4":
            pass
            ()
        elif selection == "5":
            pass
            ()
        elif selection == "6":
            pass
            ()
        elif selection == "7":
            pass
            ()
        elif selection == "8":
            print("Thank you for shopping at our store!")
            sys.exit()

        else:
            print("This feature is currently not available")


Menu()
