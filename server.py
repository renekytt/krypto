# serverprogramm
#https://docs.python.org/3/library/socketserver.html#module-socketserverimport socket
import socket,time,krüpto
# Paneme serveri kuulama porti 7482 (loodame, et see pole juba kasutuses).

serveri_aadress=(socket.gethostname(), 7842)
kuulamise_pistik = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
kuulamise_pistik.bind(serveri_aadress)
kuulamise_pistik.listen(1) #KUULAB AINULT ühte klienti


print("--Hakkan klienti ootama\n")
suhtlemise_pistik, kliendi_aadress = kuulamise_pistik.accept() #ootame kuni klient ühendab
print("--Sain just ühenduse kliendiga nr.", kliendi_aadress[0],"\n")
teade = "Tere, klient {}! Kell on {}".format(kliendi_aadress[0], time.strftime("%H:%M:%S"))
suhtlemise_pistik.sendall(teade.encode("UTF-8"))
print("--Saatsin talle sellise teate: *", teade,"*")

while True:
    vastus = suhtlemise_pistik.recv(1024).decode("UTF-8")
    if vastus=="End of communication":
        print("End of communication")
        break
    voti_dekrüpt=input("**Sisesta võti sissetulnud sõnumi dekrüpteerimiseks:__")
    print("--{}--".format(time.strftime("%H:%M:%S")), krüpto.dekrüpteeri(vastus,voti_dekrüpt))
    sonum=input("**Sisesta sõnum: ")
    if sonum=="":
        suhtlemise_pistik.send(("End of communication").encode("UTF-8"))
        break
    voti_krüpt=input("**Sisesta võti saadetava sõnumi krüpteerimiseks:__")
    suhtlemise_pistik.send(krüpto.krüpteeri(sonum,voti_krüpt).encode("UTF-8"))


