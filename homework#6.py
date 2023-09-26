# Task 1
def list_mult(list):
    mult = 1
    for i in range(len(list)):
        mult *= list[i]
    return mult

# test = [1, 2, 3, 4, 5, 6, 10]      
# test_1 = list_mult(test)
# print(test_1)

# Task 2
def min_list(list):
    return min(list)

# Task 3
def simple_numbers(list):
    count = 0
    for i in range(len(list)):
        if list[i] == 1 or list[i] == 0 or list[i] == -1:
            continue
        elif list[i] == 2 or list[i] == 3:
            count += 1
        elif list[i] % 2 == 0 or list[i] % 3 == 0:
           continue
        else:
            count += 1
    return count

# Task 4
def numbers(list, num):
    count = 0
    for i in range(len(list)):
        i -= count
        if list[i] == num:
            list.remove(list[i])
            count += 1
    return count

# Task 5
def merge(list_1, list_2):
    list_1.extend(list_2)
    return list_1

# Task 6
def degree(degree, list):
    list_1 = []
    for i in range(len(list)):
        num = list[i] ** degree
        list_1.append(num)
    return list_1

