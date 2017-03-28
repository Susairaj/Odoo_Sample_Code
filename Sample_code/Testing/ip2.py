import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("staging.tendercuts.in",80))
print s.getpeername()
print s.getsockname()
print(s.getsockname()[0])
s.close()