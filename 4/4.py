import itertools

class WeightedRoundRobinBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.server_cycle = self.weighted_round_robin()

    def weighted_round_robin(self):
        server_pool = []
        for server, weight in self.servers.items():
            server_pool.extend([server] * weight)
        return itertools.cycle(server_pool)

    def select_server(self):
        return next(self.server_cycle)

# Example usage:
servers = {'Server A': 3, 'Server B': 2, 'Server C': 1}
wrr_balancer = WeightedRoundRobinBalancer(servers)

# Simulate requests
requests = 10
for i in range(requests):
    selected_server = wrr_balancer.select_server()
    print(f"Request {i+1} routed to {selected_server}")



