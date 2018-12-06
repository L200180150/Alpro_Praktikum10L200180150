import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 1021))
print "menghitung luas balok"

while pesan.lower() != 'keluar':
    pesan = raw_input("Pesan: ")
    s.send(pesan)
    if pesan.lower() != 'keluar':
        response = s.recv(1024)
        print 'Respon: ', response
    elif pesan.lower() == 'keluar':
        respon = s.recv(1024)
        print 'Respon: -'
s.close
