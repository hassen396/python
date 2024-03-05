#accepting the message to be encriped
message=input('please enter the message to be encripted : ')

#dictionary for changing the vowel to numbers 
encryption_dict = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}

#changing goes here, vowels get replace here
half_enctyped = ''.join([encryption_dict.get(char, char) for char in message])


#and here the message is reversed
fully_encrypted=half_enctyped[::-1]
print(fully_encrypted)