
import socket as s

udp_client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

message = b"ciao"

server_address = ("192.168.65.19", 6980)
BUFFER_SIZE = 4092 #uanti bit posso inviare o ricevere

udp_client_socket.sendto(message, server_address)
data, server_address = udp_client_socket.recvfrom(BUFFER_SIZE)
print(f"Messaggio ricevuto da server: {data.decode('utf-8')} da {server_address}")