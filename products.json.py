import json

products_string = '''
{
    "products": [
        {
            "name": "Iphone 13 Pro Max Pink",
            "category": "Phone",
            "id": "1001",
            "quantity": 40,
            "color": "Pink",
            "weight": "240g",
            "size": "6.7in",
            "tech_specs": "IP68 Water Resistance, A15 Bionic chip, For more info, checkout the product's official website:https://www.apple.com/vn/iphone-13-pro/specs",
            "reviews": {"likes": 0, "dislikes": 0}
        },
        {
            "name": "Iphone 13 Blue",
            "category": "Phone",
            "id": "1002",
            "quantity": 20,
            "color": "Blue",
            "weight": "240g",
            "size": "6.7in",
            "tech_specs": "IP68 Water Resistance, A15 Bionic chip, For more info, checkout the product's official website:https://www.apple.com/vn/iphone-13-pro/specs",
            "reviews": {"likes": 0, "dislikes": 0}
        },
        {
            "name": "JBL Pulse 3",
            "category": "Audio",
            "id": "1003",
            "quantity": 40,
            "color": "Green",
            "weight": "103g",
            "size": "10in",
            "tech_specs": "add them vao nhe",
            "reviews": {"likes": 0, "dislikes": 0}
        },
        {
            "name": "JBL Pulse 4",
            "category": "Audio",
            "id": "1004",
            "quantity": 40,
            "color": "Yellow",
            "weight": "240g",
            "size": "6.7in",
            "tech_specs": "add them vao",
            "reviews": {"likes": 0, "dislikes": 0}
        }
    ]
}
'''
data = json.loads(products_string)

def displayItem():
    for product in data['products']:
        print(product['name'], product['id'], product['category'], product['color'], product['quantity'], product['size'], product['weight'], product['tech_specs'], product['reviews'] )


displayItem()
