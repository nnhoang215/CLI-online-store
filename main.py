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
