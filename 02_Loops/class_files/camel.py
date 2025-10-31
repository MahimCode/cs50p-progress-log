camel = input("camelCase: ")
snake = ""  # start with an empty string

for c in camel:
    if c.isupper():
        snake += "_" + c.lower()
    else:
        snake += c

print("snake_case:", snake)
