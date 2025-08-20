# Qno 1
# list_item = ["apple", "cherry", "orange"]
# print(list_item)

# Qno 2
# list_item = ["Pragya", True, 10]
# print(list_item)

# Qno 3
# list_item =[["apple", "cherry", "orange"], [1,2,3]]
# print(list_item)

# Qno 4, 5, 6, 7
# list_item = ["apple", "cherry", "orange"]
# first_element = list_item[0]
# middle_element = list_item[1]
# last_element = list_item[2]
# second_last_element = list_item[-1]
# print(first_element)
# print(middle_element)
# print(last_element)
# print(second_last_element)

# Qno 8,9
# numbers = [1,2,3,4,5,6]
# print(numbers[:3])
# print(numbers[3:7])

# Qno 10
# numbers = [1,2,3,4,5,6]
# reversed = numbers[::-1]
# print(reversed)

# Qno 11
# language = ["C#", "Java", "DSA"]
# language[1] = "Python"
# print(language)

# Qno 12
# text = ["Exit", "Open", "Submit"]
# text[1] = "Done"
# text[2] = "Finish"
# print(text)

# Qno 13
# course = ["BCA", "CSIT", "BBA"]
# language = ["C#", "Java", "DSA"]
# print(course + language)

# Qno 14
# course = ["BCA", "CSIT", "BBA"]
# print(course * 3)

# Qno 15
# fruits = ["apple", "banana", "cherry"]
# print("apple" in fruits)
# print("watermelon" not in fruits)

# numbers = [5,2,9,1,5,6]
# fruits = ["apple", "cherry", "banana"]

# fruits.append("orange")
# print(fruits)

# fruits.insert(0, "Kiwi")
# print(fruits)

# fruits.remove("banana")
# print(fruits)

# remove_item = numbers.pop(5)
# print(remove_item)

# remove = fruits.clear()
# print(remove)

# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# fruits.sort()
# print(fruits)

# fruits.reverse()
# print(fruits)

# print(numbers.count(5))

# fruit = fruits.index("cherry")
# print(fruit)

# print(numbers)
# num = [1,2,3,4,5,6]
# num = numbers
# print(numbers)

# Create a list of 10 numbers and get the maximum value using max() 
numbers = [1,2,3,4,5,6,7,8,9,10]
print(max(numbers))

# Create a list of 10 numbers and get the maximum value using min()
print(min(numbers)) 

# Create a list of 10 numbers and find the sum using sum()
sum = sum(numbers)
print("Sum: ",sum)

# Check if all element in a list are True using all()
check = all(numbers)
print(check)

# Check if all element in a list are True using any()
check = any(numbers)
print(check)

length = len(numbers)
print(length)

a = "apple"
b=list(a)
print(b)

tuple = (1,2,3,4)
a,b,c,d = (1,2,3,4)
print(a)

print(tuple)

a=list(range(1,5))
print(a)