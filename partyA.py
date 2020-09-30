import socket
import hashlib
import RSA
HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
print("IP of PartyA {}".format(HOST))
file = open('SampleText.txt', 'r')
datar = file.readlines()
datar = ''.join(datar)
H=hashlib.md5(datar.encode())
J=H.digest()
file1= open('HashA.txt', 'wb')
file1.write(J)
file1.close()
p = 17
q = 19
n = p*q
private_key, public_key = RSA.GenerateKeys(p, q)
encdata1 = []
for i in datar:
encdata1.append(pow(ord(i), public_key, n))
encdata1 = ' '.join([str(i) for i in encdata1])
encdata = encdata1.encode()
datar = encdata
file= open('encdata.txt','w')
file.write(encdata1)
file.close()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s.bind((HOST,PORT))
s.listen(5)
conn, addr = s.accept()
with conn:
print("Connected by Party: {}".format(addr))
while True:
conn.sendall(str(private_key).encode())
conn.sendall(datar)
break
