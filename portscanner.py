import socket
import colorama
def startmassage():
    print("#"+"*"*77+"#")
    print("| Script Name :                   Port Scanner                                |")
    print("| About Me    : [ Mohammad Abd Almoenam ] -Web Devloper- And -Ethical Hacker- |")
    print("| Facebook    :       ( https://www.facebook.com/alqnasfox )                  |")
    print("| Youtube     :  (https://www.youtube.com/channel/UCFEmcI1LJKYXgD5_PQ4rm-Q)   |")
    print("| My Website  :         ( https://alqnasfox.blogspot.com )                    |")
    print("#"+"*"*77+"#")
    print("\n")
startmassage()
colorama.init()
#difaine colors
GREEN  = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
RED    = colorama.Fore.RED 
try:
    ip         = str(input("[*] Insert Ip Adrees : "))
    startpoint = int(input("[*] Insert Start Point : "))
    endpoint   = int(input("[*] Insert End Point : "))
    scantype   = str(input("[*] Insert Type Of Scan [tcp] Or [udp] : "))
except:
    exit(f"Good By ...!")
if scantype == "tcp":
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
else:
    scantype = "udp"
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
report = ""
print(f"\nStart Scan On Ip [{ip}] With [{scantype}] Type \n")
for port in range(startpoint,endpoint):
    try:
        s.connect((ip,port))
        s.settimeout(1)
        try:
            banner = s.recv(1024)
            report = f"{GREEN}[+] Open Port [{port}] Serv [{banner}] Scantype [{scantype}] \n"
        except:
            report = f"{GREEN}[+] open port [{port}] Port Serv [{socket.getservbyport(port)}] Scantype [{scantype}] \n"
        print(report,end="")
        try:
            open(f"reports\\{ip}.txt","a").write(report[5:])
        except:pass
        #s.close()
    except KeyboardInterrupt:
        exit(f"{YELLOW}Good By ...!")
        
    except:
        print(f"{RED}[-] closed port [{port}] Scantype [{scantype}]")

s.close()
    
