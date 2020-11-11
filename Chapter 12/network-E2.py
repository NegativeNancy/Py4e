# Exercise 2: 
# Change your socket program so that it counts the number of characters it has 
# received and stops displaying any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of 
# characters and display the count of the number of characters at the end of the 
# document.

# TODO: fix that it prints words till character 3000

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

count = 0 
total = 0
while True:
    data = mysock.recv(512)
    total = total + len(data)
    if len(data) < 1:
        break
    for word in data.decode():
        if count < 3000:
            print(word)
            count += 1
        else:
            break
    # print(data.decode()[:3000])

print('Total characters in file: ', total)

mysock.close()

# Code: http://www.py4e.com/code3/socket1.py