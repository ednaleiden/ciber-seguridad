import socket



hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("el nombre del ordenador es " + hostname)
print("tu ip es " + ip)