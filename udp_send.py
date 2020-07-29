import socket
   
UDP_IP = "84.184.253.96"
UDP_PORT = 5000
MESSAGE = b"Thomas es funktioniert du bist mein HELD!!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))