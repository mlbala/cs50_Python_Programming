## Integer datatype
# -inf to +inf
# No precision - .12345
# + - * / %
# 1 + 1

# calculator 

# x = 1
# y = 2

# By default input takes input as string

# x = input("what's x? ")
# y = input("what's y? ")

# We need to convert input from default string to int
# z = int(x) + int(y)

# x = int(input("what's x? "))
# y = int(input("what's y? "))

# # z = x + y

# print(x + y)

## fload data type
# round(number[, ndigits])

x = float(input("what's x? "))
y = float(input("what's y? "))

# z = round(x + y) # nearest integer

z = x / y

# z = round(x / y, 2)
# print(z)
# print(f"{z:,})
print(f"{z:.3f}")