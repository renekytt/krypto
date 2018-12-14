# klientprogramm
#https://progeopik.cs.ut.ee/programmidevaheline_suhtlus.html#lihtne-veebiserver
import socket,time,krüpto

host="172.17.161.114" #Serveri IP kuhu soovid ühenduda
port=7842 #kokkulepitud port
serveri_aadress=(host, port)
suhtlemise_pistik = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #loob TCP ühenduse
suhtlemise_pistik.connect(serveri_aadress) #ühendume

while True: #suhtlus käib üks haaval
    vastus = suhtlemise_pistik.recv(1024).decode("UTF-8") 
    if vastus=="End of communication":
        print("End of communication")
        break
    voti_dekrüpt=input("**Sisesta võti sissetulnud sõnumi dekrüpteerimiseks:__")
    print("--{}--".format(time.strftime("%H:%M:%S")), krüpto.dekrüpteeri(vastus,voti_dekrüpt))
    sonum=input("**Sisesta sõnum: ")
    if sonum=="": #kui soovid lõpetada pead saatma tühja stringi
        suhtlemise_pistik.send(("End of communication").encode("UTF-8"))
        break
    voti_krüpt=input("**Sisesta võti saadetava sõnumi krüpteerimiseks:__")
    suhtlemise_pistik.send(krüpto.krüpteeri(sonum,voti_krüpt).encode("UTF-8"))
