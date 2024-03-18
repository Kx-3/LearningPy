# CONDITIONAL EXECUTIONS AND FUNCTIONS
name = "Abe"
if name == "John":
    print('Hello Abe')
else:
    print("I don't know you")

guy = "Keith"

match guy:
    case "Abe":
        print("Hello Abe")
    case "Keith":
        print("Hello Keith")
    case _:
        print("Hello stranger")

# Arithmetic Operators
        # // -> round
        # ** -> power
        # % -> modulus

# Logical Operators
        # or
        # and
# Comparison Operators
        # ==
        # !=
        # !
        # >
        # <
        # >=
        # <=

# Functions
# Function declaration
def add(a, b):
    return a+b #Function definition
print(add(3, 4))