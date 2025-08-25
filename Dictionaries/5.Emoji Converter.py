# Emoji Converter

messege = input("> ")
split_word = messege.split(" ")

emojis = {
    ":)" : "😀",
    ":(" : "😞"
}

output = " "
for item in split_word:
    output = output + emojis.get(item, item) + " "
print(output)