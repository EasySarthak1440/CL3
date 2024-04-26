class LeastConnectionsBalancer:
    def __init__(self, servers):
        self.servers = servers

    def select_server(self):
        min_connections = min(self.servers.values())
        least_loaded_servers = [server for server, connections in self.servers.items() if connections == min_connections]
        return least_loaded_servers[0]  # In case of ties, select the first one

    def update_connections(self, server):
        self.servers[server] += 1

# Example usage:
servers_connections = {'Server A': 10, 'Server B': 8, 'Server C': 6}
lc_balancer = LeastConnectionsBalancer(servers_connections)

# Simulate requests
requests = 5
for i in range(requests):
    selected_server = lc_balancer.select_server()
    print(f"Request {i+1} routed to {selected_server}")
    lc_balancer.update_connections(selected_server)