#!/usr/bin/env python3
import socket

if __name__ == "__main__":
    # IP and PORT on which the server is to be hosted
    IP = "127.0.0.1"
    PORT = 1234

    # Create a socket of the type (ADDRESS_FAMILY - IPV4, SOCKET_TYPE - TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set up the server - Bind the server with the IP and HOST
    server.bind((IP, PORT))
    # Listen upto 5 connections/clients
    server.listen(5)

    # Keep the server running
    while (True):
        # If a client is trying to connect using the IP and PORT of the server, accept the connection
        # Get the client object which is connected
        # and the address for the client - IP and PORT on which the client is running
        client, address = server.accept()
        """
        # My way of printing string with format method
        MESSAGE = "Connection is established - {0}:{1}"
        print(MESSAGE.format(address[0], address[1]))
        """
        print(f"Connection is established - {address[0]}:{address[1]}")

        # Receive the string (upto 1024 bytes) from client
        stringReceived = client.recv(1024)
        # Decode the string using the original encoding used
        stringReceived = stringReceived.decode("utf-8")
        # Perform some action on the string - here, convert it to the upper case
        stringUpper = stringReceived.upper()
        # Send the modified string as bytes back to client after encoding
        client.send(bytes(stringUpper, "utf-8"))
        # Close the connection with the client
        client.close()
