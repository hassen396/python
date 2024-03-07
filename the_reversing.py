# reversing a string
original_string = input('enter a string to chake if it is palindrom : ')
reversed_string = original_string[::-1]
print(reversed_string)
if original_string == reversed_string:
    print("True")
else:
    print("False")

# or can be done this way
another_reversed = reversed(original_string)
print("this is it ", ''.join(another_reversed))