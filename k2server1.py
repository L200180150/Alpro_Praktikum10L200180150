import socket
import platform

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50008))
s.listen(5)
print "Server sudah siap"
data = ''

while data.lower() != 'quit':
    komm, addr = s.accept()
    while data.lower() != 'quit':
        data = komm.recv(1024)
        if data.lower() == 'quit':
            s.close()
            break
        print 'Perintah:', data
        if data.lower() == 'machine':
            respon = platform.machine()
            komm.send(respon)
        elif data.lower() == 'release':
            respon = platform.release()
            komm.send(respon)
        elif data.lower() == 'system':
            respon = platform.system()
            komm.send(respon)
        elif data.lower() == 'version':
            respon = platform.version()
            komm.send(respon)
        elif data.lower() == 'node':
            respon = platform.node()
            komm.send(respon)
        else:
            komm.send('unknown command')
