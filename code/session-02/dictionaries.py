# create dictionary
# {<key>: <value>}
my_dict = {}
my_dict = { "type": "Car", "brand": "Ford",
"model": "Mustang", "year": 2020, 34: "34", object: "object" }
print(my_dict)

# Accession Items
model = my_dict["model"]
print(model)

print(my_dict.get("brand"))
print(my_dict.get("name", "The dict not have name"))

# Dictionary Keys
keys = my_dict.keys()
for key in keys:
    print(key)

# Dictionary Values
values = my_dict.values()
for val in values:
    print(val)

# Dictionary items
items = my_dict.items()
for key, val in my_dict.items():
    print("The key is [{}] and the value [{}]".format(key, val))
print(items)

# Change values
my_dict = { "type": "Car", "brand": "Ford", "model": "Mustang", "year": 2020, 34: "34", object: "object" }
my_dict["year"] = 2021
print(my_dict)

my_dict.update({"brand": "Toyoda"})
print(my_dict)

my_dict["name"] = "My Car"
print(my_dict)

my_dict.update({"owner": "GHC"})
print(my_dict)

# delete elems
my_dict.pop("owner")
print(my_dict)

del my_dict["name"]
print(my_dict)

del my_dict
# print(my_dict)

dict_2 = {"Dict": {"Dict": 123}}
print(dict_2)