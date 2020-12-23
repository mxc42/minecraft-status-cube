from mcstatus import MinecraftServer
import time

# Server details.
server_hostname = "mc.mxc42.com"
# The port for the query server is running on a different port than the world server.
server_port = 4243

# Make a server object with the right connection properties.
server = MinecraftServer(server_hostname, server_port)

query = server.query()

print(query.players.names)
