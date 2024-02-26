# Accepting the message to be decrypted
message = input('Please enter the message to be decrypted: ')

# Dictionary for changing the numbers back to vowels
decryption_dict = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}

# Reversing the encrypted message
half_decrypted = message[::-1]

# Changing the numbers back to vowels
fully_decrypted = ''.join([decryption_dict.get(char, char) for char in half_decrypted])

print(fully_decrypted)