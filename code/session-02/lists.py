# Create list
my_list = ["Python", "is", "so", "cool"]
my_list = []
print(my_list)

my_list = list()
my_list = list(["Python", "is", "so", "cool"])
my_list = list(("Python", "is", "so", "cool"))
print(my_list)

my_list = ["python", 23, True, "sdf", object]
print(my_list)

# len() function
size = len(my_list)
print("[+] the list have size: {}".format(size))

# Access list items
# []
my_list = ["Python", "is", "so", "cool"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[-1])
print(my_list[-2])
print(my_list[1:])
print(my_list[1:3])
print(my_list[:3])

# insert() function
my_list = ["This", "a", "list"]
my_list.insert(1, "is")
print(my_list)

# append()function
my_list = ["c#", "java", "c#"]
my_list.append("python")
print(my_list)

#remove items
my_list.remove("c#")
print(my_list)

my_list.pop(1)
print(my_list)

del my_list[1]
print(my_list)

my_list.clear()
print(my_list)

# index() function
my_list = ["Python", "is", "", "so", "cool"]
index = my_list.index("")
print("[+] {}".format(index))

# for statement
for item in my_list:
    if item == "":
        continue
    print(item)

memory_1 = ["M", "na", "i", "Jo", "Bla"]
memory_2 = ["y", "me", "s", "e"]
result = []

# for m1 in memory_1:
#     for m2 in memory_2:
#         result.append(m1+m2)

for m1, m2 in zip(memory_1, memory_2):
    result.append(m1+m2)

print(result)


sum = 89+78
average = sum/2

print(sum, average)