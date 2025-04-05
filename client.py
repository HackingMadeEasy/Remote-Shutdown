"""
THIS WAS CODED BY CRYSTALPT. PLEASE DO NOT STEAL WITHOUT CREDITS.
MAIN GITHUB LINK: https://github.com/CrystalPT
"""

# client.py (run from your remote device)
import socket

# Configuration
SERVER_IP = 'IPv4_ADDRESS'  # Change to your target's PRIVATE IP
PORT = 9876  # Same as target
PASSWORD = "your_secure_password"  # Same as target.py

def send_shutdown():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_IP, PORT))
        command = f"SHUTDOWN:{PASSWORD}"
        client.send(command.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    send_shutdown()
