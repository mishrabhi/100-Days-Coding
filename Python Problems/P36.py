# Get a string from the user and then change the first and last letter to uppercase

String = input("Enter a string: ")
String = String[0:1].upper() + String[1:len(String)-1] + String[len(String)-1:len(String)].upper()
print(String)