#The defined auxiliar function returns a list of strings with the ssids, which will be used to recover the info

def parseSSIDS():
    ssids=[]
    file="OUTPUTS/WifiPasswords/toParse.txt"
    with open(file,encoding="utf-8") as f:
        for l in f.readlines():
            if "Perfil de todos los usuarios" in l:
                ssid=l.split(":")[1].strip().strip("\r\n")
                ssids.append(ssid)
    return ssids

