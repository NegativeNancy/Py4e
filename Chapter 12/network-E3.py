# Exercise 3: 
# Use urllib to replicate the previous exercise of (1) retrieving the document 
# from a URL, (2) displaying up to 3000 characters, and (3) counting the overall 
# number of characters in the document. Don’t worry about the headers for this
# exercise, simply show the first 3000 characters of the document contents.

# TODO: item (2)

import urllib.request, urllib.parse, urllib.error

url = input("Enter URL: ")
fhand = urllib.request.urlopen(url)

count = 0
total = 0
for line in fhand:
    words = line.decode()
    total = total + len(words)
    for word in words:
        for c in word:
            if count < 300:
                count += 1
                print(c)

