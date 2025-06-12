import socket

# Function to validate port numbers
def validate_port(port_str):
    try:
        port = int(port_str)
        if 1 <= port <= 65535:
            return port
        else:
            raise ValueError
    except ValueError:
        raise ValueError("Port must be an integer between 1 and 65535.")

def main():
    print("Simple TCP Port Scanner")
    # Suggest default host and port range for compatibility
    default_host = '127.0.0.1'
    default_start_port = 65432
    default_end_port = 65432
    # Get target host from user (default: 127.0.0.1)
    target = input(f"Enter target host (default: {default_host}): ").strip() or default_host
    # Get port range from user (default: 65432-65432)
    try:
        start_port_input = input(f"Enter start port (default: {default_start_port}): ").strip()
        start_port = validate_port(start_port_input) if start_port_input else default_start_port
        end_port_input = input(f"Enter end port (default: {default_end_port}): ").strip()
        end_port = validate_port(end_port_input) if end_port_input else default_end_port
        if start_port > end_port:
            print("[!] Start port must be less than or equal to end port.")
            return
    except ValueError as ve:
        print(f"[!] Invalid port: {ve}")
        return

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    open_ports = []
    closed_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)  # Short timeout for faster scanning
            try:
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(f"[OPEN ] Port {port}")
                    open_ports.append(port)
                else:
                    print(f"[CLOSED] Port {port}")
                    closed_ports.append(port)
            except socket.gaierror:
                print(f"[!] Hostname could not be resolved: {target}")
                break
            except socket.error:
                print(f"[!] Couldn't connect to server: {target}")
                break
            except Exception as e:
                print(f"[!] Error scanning port {port}: {e}")

    print("\nScan complete.")
    print(f"Open ports: {open_ports if open_ports else 'None'}")
    print(f"Closed ports: {closed_ports if closed_ports else 'None'}")

if __name__ == "__main__":
    main()
