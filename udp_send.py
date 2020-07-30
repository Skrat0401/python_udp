import socket


UDP_IP = "127.0.0.1"
UDP_PORT = 5000

packet_description = ["cmd", "seq_no", "len", "adr0", "adr1", "data0", "data1"]    # to add more bytes just extend packet_description
packet = bytearray([0x00 for _ in packet_description])    # dynamic bytearray with lenght of packet_description

for ii, description in enumerate(packet_description):
  while True:
    try:
      packet[ii] = int(input(f"Please enter your {description}:"))
      break
    except ValueError:
      print("Input out of range!")

print(f"UDP target IP: {UDP_IP} and Port: {UDP_PORT} with message: {packet}")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto(packet, (UDP_IP, UDP_PORT))
