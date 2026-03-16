import socket
import threading

# ---------- SERVER ----------
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 54321)) # Accept connections from LAN
    server.listen(5)
    print("Server running, waiting for connection...")
    conn, addr = server.accept()
    print(f"Connected by {addr}")
    
    def receive():
        while True:
            msg = conn.recv(1024).decode()
            if msg:
                print(f"Client: {msg}")
    
    threading.Thread(target=receive).start()
    
    while True:
        msg = input()
        conn.send(msg.encode())

# ---------- CLIENT ----------
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = input("Enter server IP: ")  # e.g., 192.168.1.5
    client.connect((host_ip, 54321))
    
    def receive():
        while True:
            msg = client.recv(1024).decode()
            if msg:
                print(f"Server: {msg}")
    
    threading.Thread(target=receive).start()
    
    while True:
        msg = input()
        client.send(msg.encode())

# --------- RUN ---------
mode = input("Start as Server (S) or Client (C)? ").upper()
if mode == "S":
    start_server()
else:
    start_client()