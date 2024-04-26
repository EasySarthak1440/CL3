import Pyro4

uri = input("Enter the URI of the server object: ")
server = Pyro4.Proxy(uri)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = server.concatenate_strings(str1, str2)
print("Concatenated string:", result)
