# Task 1
def power_num(num, power):
    if power <= 0:
        return 1
    return num * power_num(num, power - 1)

# print(power_num(2, 4))

# Task 2
def star(quant) -> int:
    text = "*"
    if quant < 1:
        return ""
    return text + star(quant - 1)

# print(star(10))

# Task 3
def sum_range(a, b):
    if a == b:
        return a
    return a + sum_range(a + 1, b)

# print(sum_range(1, 10))

# Task 4 (dont know how to do)
# import random
# def weird(list):
#     sum_list = []
#     def inner():
#         sum = 0
#         if len(list) < 10:
#             return min(sum_list)
#         for i in range(10):
#             sum += list[i]
    
#         sum_list.append(sum)
#         return weird(list.pop(range(0, 10)))
#     return inner

# test = [random.randint(0, 100)]
# print(weird(test))