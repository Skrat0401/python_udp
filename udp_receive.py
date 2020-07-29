import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.setblocking(False)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(f"received message: {data} von {addr}")