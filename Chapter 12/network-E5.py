# Exercise 5: 
# (Advanced) Change the socket program so that it only shows data after the 
# headers and a blank line have been received. Remember that recv receives 
# characters (newlines and all), not lines.

# TODO: Everything

import socket

url = input("Enter URL: ")

baseUrl = url.split('/')

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((baseUrl[2], 80))
    base = 'GET HTTP/1.0\r\n\r\n'
    request = base[:4] + url + base[3:]
    cmd = request.encode()
    mysock.send(cmd)
except:
    print('Something went wrong!')
    quit()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
