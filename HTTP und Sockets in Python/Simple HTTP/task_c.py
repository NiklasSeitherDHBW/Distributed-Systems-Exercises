import socket
from urllib.parse import urlparse


def http_client(url):
    # Parse the URL
    parsed_url = urlparse(url)
    host = parsed_url.netloc
    path = parsed_url.path if parsed_url.path else '/'
    # Define the port
    port = 80
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get the IP address of the host
    remote_ip = socket.gethostbyname(host)
    # Connect to the server
    client_socket.connect((remote_ip, port))
    # Send the HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    client_socket.sendall(request.encode())
    # Receive the response
    response = b""
    while True:
        part = client_socket.recv(4096)
        if not part:
            break
        response += part
    # Close the socket
    client_socket.close()

    # Split header and body
    header, body = response.split(b'\r\n\r\n', 1)

    # Get the filename from the URL path
    filename = path.split('/')[-1]
    if not filename:
        filename = 'index.html'

    # Save the body to a file
    with open(filename, 'wb') as file:
        file.write(body)


url = input("Please enter an URL: ")
http_client(url)
