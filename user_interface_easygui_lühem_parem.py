from krüpto import *
from easygui import *
loend_sõnumitest=[krüpteeri("homme","lemon"),krüpteeri("näeme","lemon")]
def sisestus():
    sisend=multenterbox("Sisestusel kasuta tühikut või järgnevaid tähemärke:\nabcdefghijklmnopqrstuvwxyäüõö",fields=["Sõnum","Võti","IP-aadress"])
    liigutus=buttonbox("Saadetud sõnum, krüpteeritud kujul:"+ krüpteeri(sisend[0],sisend[1]),choices=["Saadan veel sõnumi","Loen sõnumeid","Lõpetan"])
    if liigutus=="Saadan veel sõnumi":
        sisestus()
    elif liigutus=="Loen sõnumeid":
        saadetud()

def saadetud():
    if loend_sõnumitest==[]:
        liigutus=buttonbox("Sõnumeid pole\nMis teha soovid?",choices=["Saadan sõnumi","Loen sõnumeid","Lõpetan"])
        if liigutus=="Saadan sõnumi":
            sisestus()
        elif liigutus=="Loen sõnumeid":
            saadetud()
    else:
        sonumid=multchoicebox("Saadetud sõnumid: ",choices=loend_sõnumitest)
        võti=enterbox("Sisesta võti: ")
        dekrüpt=""
        for i in sonumid:
            dekrüpt+=dekrüpteeri(i,võti)+"\n"
        msgbox("Sõnum on " +dekrüpt)

mida_teha=buttonbox("Tervist!\nMida te sooviksite teha?",choices=["Saadan sõnumi","Mulle saadetud sõnumid"])

if mida_teha=="Saadan sõnumi":
    sisestus()
else:
    saadetud()