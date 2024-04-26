from xmlrpc.server import SimpleXMLRPCServer

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Create an XML-RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server listening on port 8000...")

# Register the calculate_factorial function
server.register_function(calculate_factorial, "calculate_factorial")

# Run the server
server.serve_forever()
