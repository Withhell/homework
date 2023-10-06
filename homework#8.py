import re
# phone number
# numbers = ['044-235-45-14', '+380-66-078-23-45', '+38-066-078-23-45', 'incorrect', 
#            '067-235-42-88', '0992354756']

# for i in numbers:
#     if re.findall(r'^[+]?[0-9]{3}-[0-9]{2}-[0-9]{3}-[0-9]{2}-[0-9]{2}$', i) and 10 <= len(i) <= 17:
#         print(i)
#     elif re.findall(r'^[0]{1}[0-9]{9}', i):
#         print(i)
#     elif re.findall(r'^[0]{1}[0-9]{2}-[0-9]{3}-[0-9]{2}-[0-9]{2}', i):
#         print(i)
#     else:
#         print('invalid number')

# email

emails = ['Asdlk.asdlhkj30@gmail.com', 'askdja@gmail.com', 'wewbo@.gmail.com', 
          'aoidhjaoi@sdofns@gmail.com', 'hllo', 'hello@and@not.1']

for i in emails:
    if re.findall(r'@{1}\w+.\w+', i):
        print(i)
    else:
        print('invalid email')

# ПІБ
# names = ['Varhgs Cryibng Ajlf', 'Petya petya Petya', 'Astatf ashnvn3 ASJfv']
# exmpl = re.compile(r"^[A-ZА-ЯЁЇІҐЄ]{1}[a-zа-яёїієґ]{2,10}\s[A-ZА-ЯЁЇІҐЄ]{1}[a-zа-яёїієґ]{2,10}\s[A-ZА-ЯЁЇІҐЄ]{1}[a-zа-яёїієґ]{2,10}$")

# for i in names:
#     print(exmpl.match(i))