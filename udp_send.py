import socket
import struct

size = 8
list_pkt = []
ii = 1
packet = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

#"84.184.253.96"
UDP_IP = "127.0.0.1"
UDP_PORT = 5000
MESSAGE = b"Thomas es funktioniert du bist mein HELD!!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

print("Please enter your command (#1, #2, #3, #4): ")
packet[0] = int(input())
print("Please enter your sequenznumber: ")
packet[1] = int(input())

while ii < 5:
  print(f" {ii} : Please enter the adress to read or write: ")
  packet[ii + 1] = int(input())
  ii += 1

print(f"{packet}")

sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
sock.sendto(packet, (UDP_IP, UDP_PORT))