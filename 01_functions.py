# Ask user for their name
# name = input("What's your name? ")



# Say hello to user
#print("Hello,")
#print(name)
#print("hello," + name)
# print("hello,",name)

#Official documentation
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

#Named parameters
# print("hello, " , end="???")
# print(name)

# print("hello,",name, sep='--')

# print('hello, "friend"')

# Escape character
# print("hello, \"friend\"")

# print("hello, \\\\\"\\friend\"")

# print("\\n  : Newline")
# print("\\t  : Tab")
# print("\\\\  : Backslash")
# print("\\\'  : Single quote")
# print("\\\"  : Double quote")
# print("\\r  : Carriage return")
# print("\\b  : Backspace")
# print("\\101: Octal value for 'A'")
# print("\\x41: Hexadecimal value for 'A'")


#remove whitespace from string and capitalize user's name

# name = name.strip().title()

# Capitalize user's name

# name = name.capitalize()

# name = name.title()

# Remove extra spaces between words, and leading/trailing spaces
# name = ' '.join(name.split())

# stripping extra spaces, converting to title case
# name = input("What's your name? ").strip().title()

# stripping extra spaces, converting to title case, and removing extra spaces between words in one line
name = ' '.join(input("What's your name? ").strip().title().split())

# Say hello to user
print(f"hello, {name}")

