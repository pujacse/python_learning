# Reusable function:


def emoji_converter(message):
    words = message.split(" ")

    emojis = {
        ":)" : "😃",
        ":(" : "😞"
    }
    output = ""
    for item in words:
        output = output + emojis.get(item, item) + " "
    return output

message = input("> ")
print(emoji_converter(message))