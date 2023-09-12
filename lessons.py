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

