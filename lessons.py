# for i in range(5): # 0, 1, 2, 3, 4
#     # print('hello')
#     print(i, end = ' ')

# print()

# for i in range(2, 5):
#     # print('hello')
#     print(i, end = ' ')

# print()

# for i in range(1, 5, 2):
#     # print('hello')
#     print(i, end = ' ')

# print()

# start, end = 1, 10
# for i in range(start, end + 1):
#     print(i, end = ' ')

# print()

# start, end = 1, 10
# for i in range(end, start - 1, -1):
#     print(i, end = ' ')

####

# start = int(input('Enter start value: '))
# end = int(input('Enter end value: '))

# # # v1
# if start > end:
#     start, end = end, start

# # # v2 
# # if start > end:
# #     temp = start
# #     start = end
# #     end = temp

# for number in range(start, end + 1):
#     is_simple = True
    
#     if number < 2:
#         continue

#     for i in range(2, number):
#         if number % i == 0:
#             is_simple = False
#             break
    
#     if is_simple:
#         print(number, end = ' ')

################

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end='\t')
#     print()

#############

# message = 'hello world'
# message_1 = 'hello worlf'
# print(message)

# text = ("hello"
#         "world")
# print(text)

# text = '''
# qwerrty 
#     asdgw sdf
#         sadffa
# '''

# print(text)

# v1
# path = r"D:\homework#2"
# print(path)

# path = "D:\homework#2"
# print(path)

# dogs, cats = 12, 15
# result = f"Dogs {dogs} and Cats {cats}"
# print(result)

# result = "Dogs {1} and Cats".format(*args: dogs, cats)
# print(result)

# result = "Dogs {1} and Cats {0}".format(args= dogs, cats)
# print(result)

# text = "hello world. goodbye world."
# search_item = ". "

# current_index = text.find(search_item)
# print(current_index)

# first_sentence = text[:current_index + len(search_item)]
# print(first_sentence)

# second_sentence = text[current_index + len(search_item):]
# print(second_sentence)

# final_sentence = first_sentence.capitalize() + second_sentence.capitalize()
# print(final_sentence)

#####

# import random

# print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
# print(numbers)

# numbers.append(22222)
# print(numbers)

# numbers.insert(1, 33333)
# print(numbers)

# numbers.extend([2, 3, 4])
# print(numbers)

# numbers += [1, 2, 3, 4]
# print(numbers)

# numbers.remove(22222)
# print(numbers)

# del numbers
# print(numbers)

# print(numbers.index(2))

# print(numbers.pop(0))
# print(numbers)

# print(numbers.pop())
# print(numbers)

# numbers.sort()
# print(numbers)

# people = ["Tom", "bob", "alice", "Sam", "Bill"]

# people.sort()
# print(people)

# people.sort(key=str.lower)
# print(people)

# numbers = [3, 1, 4, 2, 5]

# numbers = 

#######

# import random
# words = ["Cat", "AApple", "Dog", "letter", "Helicopter"]
# secret_word = words[random.randint(0, len(words) - 1)]
# # print(secret_word)

# user_word = ["_"] * len(secret_word)
# # print(user_word)
# # print("".join(user_word))


# attempts_counter = 0

# while True:
#     if "".join(user_word).find("_") == -1:
#         print(f"\nYou guessed a word!\n Word: {secret_word}\nAttempts: {attempts_counter}")
#         break
#     print("".join(user_word))

#     letter = input("Enter letter: ").strip().lower()
#     attempts_counter += 1

#     if not letter.isalpha() or len(letter) != 1:
#         print("Pease enter only one letter!")
#         continue

#     for i in range(len(secret_word)):
#         if secret_word[i] == letter:
#             user_word[i] = letter

#############

# import random

# from random import *

# numbers = [randint(1, 30) for _ in range(10)]

# print(numbers)

# def is_simple(number: int) -> bool:
#     if number < 2:
#         return False
    
#     for num in range(2, number):
#         if number % num == 0:
#             return False
    
#     return True

# def get_simple_numbers(nums: list) -> None:
#     counter = 0
#     for number in nums:
#         if is_simple(number):
#             counter += 1
#             print(number)
            
#     return counter

##########

# def hello(): print("Hello")

# print(hello)
# message = hello
# print(message)

# hello()
# message()

# def sub(a, b): return a - b

# def add(a, b): return a + b

# def multi(a, b): return a * b

# def division(a, b): return a / b

# message = lambda: print("Hello world!")
# message()

# square = lambda side_1, side_2: side_1 * side_2
# print(square(2, 4))

# def calculate(a, b, math_operator) -> None:
#     print(f"Result: {math_operator(a, b)}")

# calculate(2, 5, lambda n1, n2: n1 + n2)
# calculate(2, 5, lambda n1, n2: n1 / n2)





