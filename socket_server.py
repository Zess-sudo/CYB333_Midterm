import socket

HOST = '127.0.0.1'
PORT = 65432  # Any number between 1024–65535

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[+] Server listening on {HOST}:{PORT}")
    
    conn, addr = s.accept()
    with conn:
        print(f"[+] Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("[!] No data received. Closing connection.")
                break
            print(f"[Client]: {data.decode()}")
            conn.sendall(b"Message received!")
