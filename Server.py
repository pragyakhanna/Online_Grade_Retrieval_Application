import socket;
import csv
import hashlib
from Authenticate import Authenticate
from hash_code import hash_credentials



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
port = 12345

#bind the socket to the host and the port
server.bind((host, port))

#Start Listening
server.listen(5)

def calc_averages(s):

    with open('Database.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        avg = 0
        if s == "GMA":
            read_col = 4
        elif s == "GL1A":
            read_col = 5
        elif s == "GL2A":
            read_col = 6
        elif s == "GL3A":
            read_col = 7
        elif s == "GL4A":
            read_col = 8
        else: 
            read_col = 0
            
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                avg += int(row[read_col])
                line_count += 1
    return avg/(line_count-1)


print_flag = 0
if (print_flag == 0):
        print("Data read from CSV File:")
        with open('Database.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    line_count += 1
                    print(f'ID number {row[0]}, Password: {row[1]}, Last Name: {row[2]}, First Name: {row[3]}, Miderm: {row[4]}, Lab 1: {row[5]}, Lab 2: {row[6]}, Lab 3: {row[7]}, Lab 4: {row[8]}')
        print_flag = 1


print(f"Listening on {host}:{port}...")


options = ["GMA","GL1A","GL2A","GL3A","GL4A"]
# Accept incoming connections

system_full = 0


while True:

    if system_full == 0:
        client_socket, client_address = server.accept() # one client connected
        system_full = 1

    
    message = client_socket.recv(1024)
    decoded_message = "N/A"

    try:
        decoded_message = message.decode('utf-8')  # Try decoding
    except UnicodeDecodeError:
        print(".")

    if decoded_message in options :
        print("Client says:", decoded_message)
        requested_average = calc_averages(decoded_message)
        client_socket.send(str(requested_average).encode('utf-8'))
        client_socket.close()
        system_full = 0
        
    else:  
        print("Client says:", decoded_message)
        record = Authenticate(message)
        if len(Authenticate(message)) > 0 :
            print("Correct Password, record found")
            client_socket.send(str(record).encode('utf-8'))
            session = 0

        elif len(Authenticate(message)) == 0 :
            client_socket.send(str("Invalid Credentials").encode('utf-8'))
        system_full = 0

server.close()   



