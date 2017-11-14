# Takes a string from the user and returns it in opposite way

word = input("Please type the word: ")

items = len(word) - 1
print("Your word is: ")
for i in range(items, -1, -1):
    print(word[i], end="")