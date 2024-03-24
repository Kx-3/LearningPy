import re
import string

with open("article.txt", mode="r") as file:
    words = file.read()
    number_pattern = r"[0-9]+\.?\,?[0-9]+"
    numbers = re.findall(number_pattern, words)
    print(numbers)
    sum = 0
    for num in numbers:
        new_num = num.replace(',', '')
        # print(new_num)
        num2 = float(new_num)
        sum += num2
        
    print(sum)
        
    