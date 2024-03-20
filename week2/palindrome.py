import string
palindrome_words = set()

def palindrome_checker(word):
    backwards_word = word[::-1]
    # backwards_word = ""
    # for i in range(len(word)):
    #     backwards_word += word[-(i + 1)]
    if backwards_word == word:
        return True
    else:
        return False
with open("palindrome.txt", mode="r") as file:
    words = file.read()
    words_list = words.split()
    for word in words_list:
        lower_word = word.lower().strip(string.punctuation)
        if palindrome_checker(lower_word):
            palindrome_words.add(lower_word)
print(palindrome_words)

# word = "abraham"
# print(word[::-1])