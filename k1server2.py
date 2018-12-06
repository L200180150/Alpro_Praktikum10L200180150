import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print "Program komunikasi tentang data diri"
data = ''
kamus = {'nama' : 'Yudha GAna Prasetyo Wibowo',
         "NIM" : 'L200180150',
         'angkatan': 'Angkatan 2018',
         'kuliah': 'Program Studi Informatika UMS'}
while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        if data.lower() == 'keluar':
            s.close()
            break
        print'Perintah:', data
        
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, perintah tidak dimengerti')    
 
