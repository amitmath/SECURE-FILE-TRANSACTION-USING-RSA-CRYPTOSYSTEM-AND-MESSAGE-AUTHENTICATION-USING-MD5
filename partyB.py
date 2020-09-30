import socket
import hashlib
import RSA
HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s.connect((HOST,PORT))
key = s.recv(20)
data = s.recv(1024)
data = data.decode()
data = data.split()
data = [int(i) for i in data]
decdata = []
p = 17
q = 19
n = p*q
private_key, public_key = RSA.GenerateKeys(p, q)
for i in data:
decdata.append(pow(i, int(key.decode()), n))
data = ''.join([chr(i) for i in decdata])
H=hashlib.md5(data.encode())
J=H.digest()
file1= open('HashB.txt', 'wb')
file1.write(J)
file1.close()
file = open('recdata.txt', 'w')
print('\n Data received at revdata.txt')
file.write(data)
file.close()
count=0
with open('HashA.txt') as f1, open('HashB.txt') as f2:
for l1, l2 in zip(f1, f2):
if l1!=l2:
count=1
if(count==0):
print("\n ~MESSAGE RECIEVED IS AUTHENTIC AND HAS NOT
BEEN MODIFIED~")
