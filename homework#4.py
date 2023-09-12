# Task 1
text = str(input("Enter some text: "))
count_num = 0
count_lett = 0
i = 0
for i in range(len(text)):
    if text[i].isnumeric() == True:
        count_num += 1
    elif text[i].isalpha() == True:
        count_lett += 1
    else:
        continue
    i += 1
print(f"Numbers: {count_num}", f"Letters: {count_lett}")

# Task 2
text = str(input("Enter some text: "))
sym = str(input("Enter symbol you want to find: "))
i = 0
count = 0
for i in range(len(text)):
    if text[i] == sym:
        count += 1
    i += 1
print(count)

# Task 3

sent = str(input("Enter a sentence: "))
word = str(input("Enter a word you wish to replace: "))
repl = str(input("Enter a replacement: "))
print(sent.replace(word, repl))

# Task 4

text = str(input("Enter some text: "))
print(text[2])
print(text[len(text) - 1])
print(text[:5])
print(text[:len(text) - 2])
print(text[::2])
print(text[1::2])
print(text[::-1])
print(text[::-2])
print(len(text))

# Optional
text = "I want to break free 1. I'm free 2!"

sent_1 = text[:text.find(". ") + 1]
sent_2 = text[text.find(". ") + 1:]

print(sent_1.capitalize(), sent_2.capitalize())

count_punct = 0
count = 0
count_excl = 0
for i in range(len(text)):
    if text[i].isnumeric() == True:
        count += 1
    elif text[i] == "." or text[i] == "," or text[i] == "?" or text[i] == ":" or text[i] == ";":
        count_punct += 1
    elif text[i] == "!":
        count_excl += 1
        count_punct += 1
print(f"Number of numbers in sentences: {count}", "\n", 
      f"Number of punctuation: {count_punct}\n",
      f"Number of exclamation marks: {count_excl}")

    




