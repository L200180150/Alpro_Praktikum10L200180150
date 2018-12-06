import socket

def l(p=0, t=0, l=0):
        l = 2 * (p*l + p*t + l*t)
        return l

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 1021))
s.listen(5)

print "Server sudah siap"
data = ''

while l:
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)

        print 'Pesan :', data
        if data.find("paramater") != -1:
                
            param, value = data.split("=")           
            if param == "paramater1":
                p = float(value)
                x = value


                komm.send("Paramater panjang dicatat")
            elif param == "paramater2":
                t = float(value)
                y = value
                komm.send("Paramater tinggi dicatat")
            elif param == "paramater3":
                l = float(value)
                y = value
                komm.send("Paramater lebar dicatat")
            elif data == 'hitung':
                komm.send("Luas balok dengan panjang {}, tinggi {} dan lebar {} adalah{}"
                          .format(LP = 2 * (p*l + p*t + l*t)))

            else:
                komm.send("Tidak ada")
                
