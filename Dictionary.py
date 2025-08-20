# Basic
# data = {
#     "name": "John",
#     "age": 25,
#     "city": "London"
# }
# print(data)
# print(data["age"])

# data["country"] = "UK"
# print(data)

# data["city"] = "Paris"
# print(data)

# del data["age"] 
# print(data)

# Meduim Qno 1
# data = {
#     "name": "Sam",
#     "salary": 5000
# }
# a=data.get("salary")
# print(a)

# Qno 2
# dict_one = {
#     1: "a",
#     2: "b"
# }
# dict_two = {
#     3: "c",
#     4: "d"
# }
# merge_dict = dict_one | dict_two
# print(merge_dict)

# Qno 3
# my_dict = {
#     "name": "Pragya",
#     "age": 21
# }
# keys = my_dict.keys()
# values = my_dict.values()

# print("Keys: ", keys)
# print("Values: ", values)

# Qno 4
# keys = ["a", "b", "c"]
# values = [1,2,3]
# my_dict = dict(zip(keys, values))
# print(my_dict)

# Qno 5
# fruit = "Banana"
# my_dict = {
 
# }
# for i in fruit:
#     count1 = fruit.count(i)
#     my_dict[i] = count1

# print(my_dict)

# Qno1
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 30
# }
# max_key = max(data, key=data.get)
# print("Key with the maximum value: ", max_key)

# Qno 2
data = {"a": 1, "b": 2, "c": 3}

inverted = {v: k for k, v in data.items()}
print("Inverted dictionary:", inverted)

# Qno 3
students = {
    "S1": {
        "name": "Ritika",
        "math": 78
    },
    "S2" :{
        "name": "Rosna",
        "math": 81
    },
    "S3" :{
        "name": "Rojan",
        "math": 88
    }
}
print("Students scoring more than 80 in math: ")
for details in students.values():
    if details["math"]>80:
        print(details["name"])


