def krüpteeri(sisend,võti):
    tähestik=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"," "]
    võti_õige_pikkusega=pikkused_samaks(sisend,võti)
    sisend=sisend.lower()
    krüpteeritud=""
    for i in range(len(sisend)):
        krüpteeritud+=tähestik[(tähestik.index(võti_õige_pikkusega[i])+ tähestik.index(sisend[i]))%27]
    return krüpteeritud

def dekrüpteeri(krüpteeritud,võti):
    tähestik=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"," "]
    võti_õige_pikkusega=pikkused_samaks(krüpteeritud,võti)
    krüpteeritud=krüpteeritud.lower()
    dekrüpteeritud=""
    for i in range(len(krüpteeritud)):
        dekrüpteeritud+=tähestik[(tähestik.index(krüpteeritud[i])-tähestik.index(võti_õige_pikkusega[i]))%27]
    return dekrüpteeritud

def pikkused_samaks(esimene,teine):
    a=len(esimene)//len(teine)
    b=len(esimene)%len(teine)
    teine=teine*a+teine[0:b]
    return teine.lower()
