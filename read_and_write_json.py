import json

def write_json(data, file_name="products.json"):
    with open(file_name, "w") as f:
            json.dump(data, f, indent=4)
    
with open("products.json") as json_file:
    data = json.load(json_file)
    temp = data["products"]
    y = {"": "Joe", "age": 40}
    temp.append(y)
    print(data["name"][0])

write_json(data)