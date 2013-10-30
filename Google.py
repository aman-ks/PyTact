import urllib2

url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-IN"
audio = open('output.flac','rb').read()
headers={'Content-Type': 'audio/x-flac; rate=16000', 'User-Agent':'Mozilla/5.0'}
request = urllib2.Request(url, data=audio, headers=headers)
response = urllib2.urlopen(request)
print response.read()
