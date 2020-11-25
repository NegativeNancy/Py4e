import urllib.request, urllib.parse, urllib.error
import json, ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')

    content = json.loads(data)
    print('Count:', len(content['comments']))

    total = 0
    for item in content['comments']:
        total += int(item['count'])
    
    print('Sum:', total)
