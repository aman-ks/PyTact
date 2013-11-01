import urllib2
import os
import sys

audio = open(sys.argv[1], 'rb')
filesize = os.path.getsize(sys.argv[1])

print sys.argv[1],"Read","\n"

req = urllib2.Request(url='https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US')
req.add_header('Content-type','audio/x-flac; rate=16000')
req.add_header('Content-length', str(filesize))
req.add_data(audio)

print "Request built","\n"

response = urllib2.urlopen(req)

print "Response returned","\n"

print response.read()
