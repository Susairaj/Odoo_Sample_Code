import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("clean-erp.com",80))
print s.getpeername()
print s.getsockname()
print(s.getsockname()[0])
s.close()