def calc(operator, var1, var2):
    if (operator == 'x'):
        print(var1 * var2)
    elif (operator == '+'):
        print(var1 + var2)
    elif (operator == '-'):
        print(var1 - var2)
    elif (operator == '/'):
        print(var1 / var2)
    else:
        print("Invalid operator")

# calc('+', 1, 2)
# calc('/', 5, 2)
# calc('x', 5, 0)

with open("file.txt",'r') as f:
    text_strings = f.read().splitlines()
    for text_string in text_strings:
        fred = text_string.split()

        if fred[0] == "calc":
            # call calc
            operator = fred[1]
            var1 = fred[2]
            var2 = fred[3]
            calc(operator, var1, var2)
        else:
            print("invalid command")

            #
        # print(text_string)
f.close()
