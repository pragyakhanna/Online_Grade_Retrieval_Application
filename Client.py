import socket
import hashlib
import getpass
from Authenticate import Authenticate
from hash_code import hash_credentials

# Server details
host = 'localhost'  # Must match the server's host
port = 12345        # Must match the server's port

connected = 0
session_id_hashed = 0

while True:
    # Get user command
    if connected == 0:
        command = input("Enter Command: ")
        print(f'Command Entered: {command}')  # Echo command back
        # Check the command
        if command == "GMA":
            print("Fetching Midterm Average:")
        elif command == "GL1A":
            print("Fetching Lab 1 Average:")
        elif command == "GL2A":
            print("Fetching Lab 2 Average:")
        elif command == "GL3A":
            print("Fetching Lab 3 Average:")
        elif command == "GL4A":
            print("Fetching Lab 4 Average:")
        elif command == "GG":
            print("Authenticate yourself")
        elif command.lower() == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid command")
            continue  # Ask for another command without attempting to connect

    
    if command != "GG" and connected == 0:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            print(f'Connected to {host} at port {port}')

            # Send the command
            client_socket.send(command.encode('utf-8'))

            # Receive response
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Server disconnected.")
            else:
                print("Server Responded with:", message)
            client_socket.close()


    elif command == "GG" and connected == 0:
            Username = input("Enter Username: ")
            Password = input("Enter Password: ")
            combined_input = Username + ":" + Password  
            hashed_data = hash_credentials(combined_input)
            session_id_hashed = hashed_data
            print(f'Hash sent to the server {hashed_data}')
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            print(f'Connected to {host} at port {port}')
            # Send the commandG
            client_socket.send(hashed_data)
            # Receive response
            message = client_socket.recv(1024).decode('utf-8')

            if not message:
                print("Server disconnected.")
            else:
                print("Server Responded with:", message)
            client_socket.close()



    

         
         

    
