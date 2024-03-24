import re

email = "johndoe@gmail.com"
number = "305 555-1234"
sentence = "I have the following emails: kipkiruiketer755@gmail.com, kipkiruiketer01@gmail.com, zinduaschool@outlook.org, abeisacoustic@hotmail.com."

# ^ -> start of the string
# [a-z] -> small letters only from a-z
# [a-zA-Z0-9] -> checking for characters and numbers inside the brackets
# | -> 

email_pattern = r"\b[a-zA-Z0-9]+@(?:gmail|hotmail|outlook)+.(?:com|org)"
pattern = r"\b[a-z]+@(?:gmail|yahoo|hotmail)+\.(?:com|net|org)"
number_pattern = r"^\d{3}\ +\d{3}\-+\d{4}$"

print(re.findall(email_pattern, sentence))

# if re.match(number_pattern, number):
#     print("Valid number")
# else:
#     print("Invalid number")