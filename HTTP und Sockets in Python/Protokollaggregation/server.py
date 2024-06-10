import socket

def udp_server(host='0.0.0.0', port=6001):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the address and port
    server_address = (host, port)
    sock.bind(server_address)
    print(f'Server listening on {host}:{port}')

    while True:
        try:
            # Receive message from client
            data, address = sock.recvfrom(4096)
            print(f'Received {data.decode()} from {address}')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    udp_server()
