#!/usr/bin/env python3

import socket

if __name__ == "__main__":
    # IP and PORT on which the server is running
    IP = "127.0.0.1"
    PORT = 1234

    # Create a socket of the type (ADDRESS_FAMILY - IPV4, SOCKET_TYPE - TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect (NOT BIND) to the socket/server which is running at IP and PORT
    server.connect((IP, PORT))

    # Get user input from the command line
    myString = input("Enter string: ")

    # Send the string to the server as bytes after encoding
    server.send(bytes(myString, "utf-8"))
    # Receive the response from the server
    buffer = server.recv(1024)
    # Decode the response with the original encoding used
    buffer = buffer.decode("utf-8")
    # Print the response from the server
    print(f"Server: {buffer}")
