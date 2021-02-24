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


