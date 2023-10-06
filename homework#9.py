# Tasks
with open('homework.txt', 'w') as test:
    test.write(
        "To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep"
    )
with open('homework.txt', 'r') as test:
    text = test.readline()
    punc_list = ['!', '(', ')', '-', '[', ']', '{', '}', ';', ':', '\'', '\"', '\\', ',', '<', '>', '.', '/', '?', '@', '#', '$', '%', '^', '&', '*', '_', '~']
    for i in punc_list:
        text.replace(i, "")
    # text = text.replace(",", "")
    # text = text.replace("?", "")
    # text = text.replace("!", "")
    # text = text.replace(".", "")
    text_list = text.split(" ")
    print(text_list)
    with open('7 letters.txt', 'w') as home:
        for i in range(len(text_list)):
            if len(text_list[i]) >= 7:
                home.write(text_list[i])
                home.write(", ")

print(f"Number of words in text: {len(text_list)}")

# Optional

with open('optional.txt', "w") as file:
    text = "To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, " \
            "Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end" \
            "The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep"
    cursed_word = 'die'
    count = text.count(cursed_word)
    star = '*' * len(cursed_word)
    txt = text.replace('die', star)
    file.write(txt)
    print(count)