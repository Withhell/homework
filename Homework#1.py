# Ex.1
a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the second number"))
print('Sum: ', a + b + c, '\n', 'Multi: ',  a * b * c, )

# Ex.2 
d_1 = float(input('enter length of the first diagonal'))
d_2 = float(input('enter length of the second diagonal'))
print('S = ', 0.5 * d_1 * d_2)

# Ex.3.1
n = input('enter 4-digit number')
print(int(n[0]) * int(n[1]) * int(n[2]) * int(n[3])) 
# Ex.3.2
n = int(input('enter 4-digit number'))
n1 = n // 1000
n2 = n // 100 % 10
n3 = n // 10 % 10
n4 = n % 10
print(n1 * n2 * n3 * n4)