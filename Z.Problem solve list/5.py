# Word frequency Counter - Count the frequency of words in a given sentence using a dictionary.
# Example:
# my name is puja puja is pagla puja
# my : 1
# name : 1
# is : 2
# puja : 3
# pagla : 1

sentence = input("Enter sentence: ")

words = sentence.split()
print(words)

thisdict = {

}

for word in words:
    if word in thisdict:
        x = thisdict.get(word)
        x += 1
        thisdict[word] = x
    else:
        x = 1
        thisdict[word] = x

print("Word frequency: ")
for word,freq in thisdict.items():
    print(f"{word}: {freq}")