import string
with open("words.txt", mode="r") as words:
    words_list = words.read().lower().split()
    word_dict = {}
    
    for word in words_list:
        # mytable = str.maketrans('', '', string.punctuation)
        # new_word = word.translate(mytable)
        new_word = word.strip(string.punctuation)
        if new_word not in word_dict :
            word_dict[new_word] = 1
        else:
            word_dict[new_word] = word_dict[new_word] + 1
    print(word_dict)

