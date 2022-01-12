import json

def write_json(data, file_name="products.json"):
    with open(file_name, "w") as f:
            json.dump(data, f, indent=4)
    
with open("products.json") as json_file:
    data = json.load(json_file)
    temp = data["products"]
    list_dict = data["products"]

write_json(data)