from mcstatus import MinecraftServer

# Server details.
server_hostname = "mc.mxc42.com"
server_port = 4242

# Make a server object with the right connection properties.
server = MinecraftServer(server_hostname, server_port)

# 'query' has to be enabled in a servers' server.properties file.
# It may give more information than a ping, such as a full player list or mod information.
query = server.status()

print(query.players.online)
