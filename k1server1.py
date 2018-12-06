import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print "Program komunikasi tentang data diri"
while pesan.lower() != 'keluar':
    pesan = raw_input('perintah:')
    s.send(pesan)
    if pesan.lower() != 'keluar':
        response = s.recv(1024)
        print 'Jawab:', response
    else:
        print 'siap!!!'
        s.close()
