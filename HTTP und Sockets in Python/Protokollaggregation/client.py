import socket
from configuration import SERVER_HOST, SERVER_PORT

def udp_client(server_host=SERVER_HOST, server_port=SERVER_PORT):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (server_host, server_port)
    
    while True:
        try:
            # Get user input
            message = input("Enter message to send to server: ")
            if message.strip():  # Validate input
                # Send message to server
                sent = sock.sendto(message.encode(), server_address)
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    udp_client()
