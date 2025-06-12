import socket

HOST = '127.0.0.1'  # Server address (localhost)
PORT = 65432        # Port must match the server's port
MESSAGE = "Hello, server!"  # Message to send

def main():
    """
    Connects to the server, sends a message, and prints the server's response.
    Handles errors gracefully.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((HOST, PORT))
            print(f"[+] Connected to server at {HOST}:{PORT}")
            client_socket.sendall(MESSAGE.encode('utf-8'))
            print(f"[>] Sent: {MESSAGE}")
            response = client_socket.recv(1024)
            print(f"[<] Received: {response.decode('utf-8')}")
        except ConnectionRefusedError:
            print(f"[!] Could not connect to server at {HOST}:{PORT}. Is the server running?")
        except socket.error as err:
            print(f"[!] Socket error: {err}")
        except Exception as exc:
            print(f"[!] Unexpected error: {exc}")

if __name__ == "__main__":
    main()
