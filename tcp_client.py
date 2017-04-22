import socket

target_host = "0.0.0.0"
target_port = 9999

#sock object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client connection
client.connect((target_host, target_port))

#send data
client.send("ABCDEF")

#receive data
response = client.recv(4096)

print response