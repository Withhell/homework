# git init -> create git repository 
# print('hello world')
# print('i dont understand')

####################
# v1 

# n1 = 10  + 20 * 2 # оператор присвоєння, обробляється останнім
# n2 = 20 

# v2
# n1, n2 = 10, 20 # множинне присвоєння

# is_valid = False
# print(is_valid)
# print(not is_valid) # not -> inversion

# print('hello' in 'hello world')

##################
# hours = int(input('Enter hours: '))

# # # v1
# # if hours >= 12:
# #     print('PM')
# # else:
# #     print('AM')

# # v2

# if hours >= 12 and hours < 24: # if 12 <= hours < 24:
#     print('PM')
# elif hours >= 0 and hours <= 24:
#     print('AM')
# else:
#     print('Error')

# ввести рейтинг фільму: якщо рейтинг 5 або 4 - ок, інакше - погано

# film_rating = int(input('Enter film rating'))

# if 0 < film_rating <= 5:
#     if film_rating == 4 and film_rating == 5:
#         ptint('ok')
#     else:
#         print('Not ok')
# else:
#     print('incorrect rating')

#################

# print('merge conflict example')
# print('Hello!')

# print('Some text')

# print('more text')

##################
# try:
#     print('1. Start game\n2. Settings\n3. Saved games\n4. Exit')
#     user_select = int(input('Enter menu number: '))

#     # v1
#     if user_select == 1:
#         print('Game started')
#     elif user_select == 2:
#         print('Settings opened')
#     elif user_select == 3:
#         print('Saved games opened')
#     elif user_select == 4:
#         print("Exit...")
#     else:
#         print('incorrect menu item!')
    
#     # v2
#     match user_select:
#         case 1:
#             print
#         case 2:
#             print
#     ......
#except Exception as e:
#   print(f'Error: {e}')

##################

# Cycles

# v1
# i = 0

# while i < 10:
#     print(i, end = " ")
#     i += 1


# print('test')

# v2

# i = 12

# while True:
#     print(i)
#     i += 2

# v3
# i = 0

# while True:
#     if i == 5:
#         print('continue...')
#         i += 1
#         continue

#     if i >= 10:
#         print('break....')
#         break

#     print(i)
#     i += 1


############################

# count = 0
# sum = 9
# try:
#     while True:
#         try:
#             user_number = int(input('Enter number: '))
            
#             if user_number == 0 and count == 0:
#                 print('end....')
#                 continue

#             if user_number == 0:
#                 print('end...')
#                 break

#             sum += user_number
#             count += 1
#         except ValueError as e:
#             print('Enter number only')
            
#     print(f'Sum: {sum}')
#     print(f'Avg: {sum / count}')
# except Exception as e:
#     print(e)
