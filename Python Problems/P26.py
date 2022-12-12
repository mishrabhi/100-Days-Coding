# Get the number of people in the room as input from the user. Then calculate the maximum number of handshakes possible among that people.

n = int(input("Enter number of men: "))
no_of_handshakes = int(n * ((n - 1) / 2))
print("Maximum number of handshakes possible for", n , 'people are', no_of_handshakes)