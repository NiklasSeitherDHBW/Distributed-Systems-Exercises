import socket
from urllib.parse import urlparse


def http_client(url):
    # Parse the URL
    parsed_url = urlparse(url)
    host = parsed_url.netloc
    path = parsed_url.path if parsed_url.path else '/'
    # Define connection parameters
    port = 80
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((host, port))
    # Send the HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    client_socket.sendall(request.encode())
    # Receive the response
    response = client_socket.recv(4096)
    print(response.decode())
    # Close the socket
    client_socket.close()


url = input("Please enter an URL: ")
http_client(url)
