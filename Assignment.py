# # Length and Indexing
quote = "Hello World"

# print(len(quote))
# print(quote[0])
# print(quote[-1])

# # Concatenation
# fname = "Pragya"
# lname = "Shrestha"

# print("My name is ", fname +" " + lname)

# # Repetition
# print("Python" * 10)

# # Convert "learning python" 
# convert = "learning python"

# print(convert.upper())
# print(convert.lower())
# print(convert.title())

# # Remove spaces from "Clean me"
# text = " Clean me "
# print(text.replace(" ",""))

# # Replace "dog" with "cat" in "I have a dog"
# text = "I have a dog."
# a= text.replace("dog", "cat")
# print(a)

# # Count how many times "a" appears in "Banana"
# text = "Banana"
# print(text.count("a"))

# # Slicing & Substrings
# # Extract "thon" from "Python"
# text = "Python"
# print(text[2:6])

# # From "I love programming", extract "love"
# text = "I love programming"
# print(text[2:6])

# # Reverse the string "Python" using slicing
# text = "Python"
# a=text[::-1]
# print(a)

# # Escape Character
# print("ngin \nCopyEdit \nHello \nWorld")
# print("makefile \nCopyEdit \nName:John \nAge:25")

# # Searching
# # Check if "Python" is present in "I love python programming"
# text = "I love Python Proramming"
# word = "Python"
# if(word == "Python"):
#     print("Word is found")

# # Find the index of "code" in "Let's code in python"
# text = "Let's code in Python"
# print(text.index("code"))

# # Formatting
# age = 20
# print(f"My name is Pragya and i am {age} years old.")

# # Use .format() to print
# temp = 30
# print("Temperature toady is {} C".format(temp)) 

# # Take a string from the user
# # text = input("Enter a string:")

# # reversetxt = text[::-1]
# # print("Reversed string:", reversetxt)

# # if(text == reversetxt):
# #     print("The string is a palindrome")
# # else:
# #     print("The string is not a palindrome.")

# # Ask the users for a sentence and count the number of words
# # text = input("Enter your name:")
# # print(len(text.split()))

# # Replace all vowels in a string with "*"
# # text = input("Enter a string: ")
# # vowels = "aeiouAEIOU"

# # for i in vowels:
# #     text=text.replace(i,'*')
# # print(text)

# # Creative Task
# # Word Replacer
# text = input("Enter a sentence: ")
# text = text.replace("Hi", "Hello")
# print("Modified sentence: ", text)

# Abbreviation Marker
# text = input("Sentence: ")
# text = text.split()

# answer =""
# for i in text:
#     answer += i[0]
# print("Abbreviation: ", answer)

# Caesar Cipher


# Username Generator
# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")
# year = input("Enter your birth year: ")
# print(fname + "." + lname + "." + year)

# Password Generator
# import random
# word = input("Enter your word: ")
# word_reverse = word[::-1]
# upeer_word = word.upper()
# a=str(random.randint(3, 9))

# print(word_reverse + upeer_word + a)


#Pig Latin Convertor
# text = "Python"
# new_text = text[1:] + text[0]
# print(new_text)
