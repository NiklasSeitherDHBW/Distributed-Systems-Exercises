import socket

def http_client():
    # Define connection parameters
    host = 'www.michael-eichberg.de'
    port = 80
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((host, port))
    # Send the HTTP GET request
    request = f"GET /index.html HTTP/1.1\r\nHost: {host}\r\n\r\n"
    client_socket.sendall(request.encode())
    # Receive the response
    response = client_socket.recv(4096) # chunk_size=1024 from lecture is not enough
    print(response.decode())
    # Close the socket
    client_socket.close()

# Run the HTTP client
http_client()
