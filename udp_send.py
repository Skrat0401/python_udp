import socket

size = 8
list_pkt = []

packet = bytearray(size)

UDP_IP = "84.184.253.96"
UDP_PORT = 5000
MESSAGE = b"Thomas es funktioniert du bist mein HELD!!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
print("Please enter your command: ")
commandobyte = input()
print("Please enter your sequenznumber: ")
sequenz = input()
print("Please enter the adress to read or write: ")
adr = input()
print(f"{packet}")
list_pkt = commandobyte


sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))