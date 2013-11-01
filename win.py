import urllib2
import os
import sys

def func(filename):    
    audio = open(filename, 'rb')
    filesize = os.path.getsize(filename)

    print filename,"Read","\n"

    req = urllib2.Request(url='https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US')
    req.add_header('Content-type','audio/x-flac; rate=16000')
    req.add_header('Content-length', str(filesize))
    req.add_data(audio)

    print "Request built","\n"

    response = urllib2.urlopen(req)

    print "Response returned","\n"

    return response.read()
