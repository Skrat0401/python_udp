import socket

size = 8
list_pkt = []
ii = 1
packet = bytearray(size)

UDP_IP = "84.184.253.96"
UDP_PORT = 5000
MESSAGE = b"Thomas es funktioniert du bist mein HELD!!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

print("Please enter your command (#1, #2, #3, #4): ")
commandobyte = int(input())
print("Please enter your sequenznumber: ")
sequenz = int(input())
list_pkt.append(commandobyte)
list_pkt.append(sequenz)

while ii < 4:
  print("Please enter the adress to read or write: ")
  adr = int(input())
  list_pkt.append(adr)
  ii += 1

print(f"{packet}")
print(f"Type:{type(commandobyte)}")
packet = bytearray(list_pkt)

print(f"{packet}")

sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
sock.sendto(packet, (UDP_IP, UDP_PORT))