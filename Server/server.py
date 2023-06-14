import socket
import os
import psutil
from functions.utils.client_helpers import handle_client

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

running: bool = True

max_memory_usage = 500 * 1024 * 1024 # Sets the maximum memory usage in bytes (500 MB)
max_cpu_usage = 90 # Sets the maximum CPU usage in percentage

while running:
    # Gets the current memory usage of the process
    memory_usage = psutil.Process(os.getpid()).memory_info().rss
    
    # Checks if memory usage has exceeded the maximum limit
    if memory_usage > max_memory_usage:
        print("Exceeded maximum memory usage, terminating the server")
        running = False
        break
    
    # Get current CPU usage
    cpu_usage = psutil.cpu_percent()
    
    # Checks if CPU usage has exceeded the maximum threshold
    if cpu_usage > max_cpu_usage:
        print("Exceeded maximum CPU usage, terminating the server")
        running = False
        break

    # Wait for a connection
    print('waiting for a connection')
    client_socket, client_address = server_socket.accept()
    
    try:
        print('connection from', client_address)
        
        # Send welcome message
        welcome_message = "Welcome!"
        client_socket.send(welcome_message.encode())
        
        # Handle client connection
        handle_client(client_socket)
        
    finally:
        # Clean up the connection
        client_socket.close()
