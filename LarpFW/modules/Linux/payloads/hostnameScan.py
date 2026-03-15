import socket,pickle

def hostnameScan(HOST,PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST,PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("\033[32m[+]\033[0m Connected to RHOST!")
            cmd = ["hostname -I", "__eoc__"]
            cmd2 = pickle.dumps(cmd)
            conn.sendall(cmd2)
            print("\033[32m[+]\033[0m Sent payload to RHOST!")
            data = b""
            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                data += chunk
            print("\033[32m[+]\033[0m STDOUT recieved:\n", data.decode(errors="ignore"))
            s.close()

if __name__ == "__main__":
    pass
    