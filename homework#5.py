import random

# Task 1

list = []
list_SIZE = int(input("How long do you want the list: "))
evensum = 0
oddsum = 0
negsum = 0
three = 1
minmax = 1
first_index = 0
last_index = 0
pos = 0


for i in range(list_SIZE):
    list.append(random.randint(-100, 100))


for y in range(len(list)):
    if list[y] < 0:
        negsum += list[y]
    if list[y] % 2 == 0:
        evensum += list[y]
    if list[y] % 2 == 1:
        oddsum += list[y]
    
for i in range(list_SIZE):
    if list[i] % 3 == 0:
        three *= list[i]


min = list.index(min(list))
max = list.index(max(list))

for i in range(min + 1, max):
    minmax *= list[i]


for i in range(list_SIZE):
    if list[i] >= 0:
        first_index = i
        break


for i in range(first_index + 1, list_SIZE):
    if list[i] >= 0:
        last_index = i
        break


for i in range(first_index + 1, last_index):
    pos += list[i]


print(f"Sum of negative numbers: {negsum}\n", 
       f"Sum of positive numbers: {evensum}\n",
       f"Sum of odd numbers: {oddsum}\n",
       f"Multiplied numbers between min and max: {minmax}\n", 
       f"Multiplied numbers that are multioles of 3: {three}\n", 
       f"Sum of numbers between first and last positive numbers: {pos}\n")

# Task 2

numbers = []
num_size = int(input("How long do you want the list: "))
odd = []
even = []
neg = []
pos = []
for i in range(num_size):
    numbers.append(random.randint(-100, 100))

for i in range(num_size):
    if numbers[i] % 2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])

for i in range(num_size):
    if numbers[i] < 0:
        neg.append(numbers[i])
    else:
        pos.append(numbers[i])

print(f"List of even numbers: {even}\n",
      f"List of odd numbers: {odd}\n",
      f"List of positive numbers: {pos}\n",
      f"List of negative numbers: {neg}\n")