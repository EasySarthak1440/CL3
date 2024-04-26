import Pyro4

@Pyro4.expose
class StringConcatenationServer:
    def concatenate_strings(self, str1, str2):
        return str1 + str2

daemon = Pyro4.Daemon()
uri = daemon.register(StringConcatenationServer)

print("Server ready. URI =", uri)
daemon.requestLoop()
