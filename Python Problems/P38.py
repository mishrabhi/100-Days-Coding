string = input("Enter a string: ")

# Create a dictionary to store the frequency of each character
char_freq = {}

# Iterate through the string and update the frequency of each character in the dictionary
for char in string:
  if char in char_freq:
    char_freq[char] += 1
  else:
    char_freq[char] = 1

# Iterate through the string again and print the non-repeating characters
for char in string:
  if char_freq[char] == 1:
    print(char,end="")