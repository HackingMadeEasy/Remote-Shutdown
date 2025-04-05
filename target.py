# target.py (runs on PC you want to shut down)
import socket
import os
import threading
import hashlib
import time

# Configuration
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 9876  # Choose an unused port
PASSWORD = "your_secure_password"  # Change this!

def handle_client(client_socket):
    # Receive command
    data = client_socket.recv(1024).decode('utf-8').strip()
    
    # Split command and password
    try:
        command, password_attempt = data.split(':', 1)
    except ValueError:
        client_socket.send("Invalid command format".encode('utf-8'))
        client_socket.close()
        return
    
    # Verify password (use a more secure method in production)
    if hashlib.sha256(password_attempt.encode()).hexdigest() != hashlib.sha256(PASSWORD.encode()).hexdigest():
        client_socket.send("Authentication failed".encode('utf-8'))
        client_socket.close()
        return
    
    # Process command
    if command == "SHUTDOWN":
        client_socket.send("Shutting down...".encode('utf-8'))
        client_socket.close()
        # Delay to allow response to be sent
        time.sleep(1)
        # Execute shutdown
        os.system("shutdown /s /t 10")  # Windows
        # For Linux: os.system("shutdown -h now")
    else:
        client_socket.send("Unknown command".encode('utf-8'))
    
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Listening on {HOST}:{PORT}")
    
    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()
