import socket
host = '192.168.1.23'
port = 5050
timeout=3
try:
    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
except Exception as ex:
    print ex.message
True
