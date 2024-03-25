import requests

with open('test.html', 'wb') as f:
    f.write(requests.get('http://rubin.kodeks.ru:777/file/0230bf32f85099a57ae53adb77d8a84e').content)