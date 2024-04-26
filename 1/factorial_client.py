import xmlrpc.client

# Connect to the XML-RPC server
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input the number from the user
n = int(input("Enter a number: "))

# Call the remote method on the server
result = server.calculate_factorial(n)

# Print the result
print(f"Factorial of {n} is: {result}")
