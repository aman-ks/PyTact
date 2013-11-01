import sys
import urllib

_base_url = 'https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-IN&maxresults=1'
_filepath = '/aman/output.flac'
           
post_data = {'Content_Type' : 'audio/x-flac; rate=16000', 'Content' : open(_filepath, mode="rb") }
request = urllib.urlopen(_base_url, urllib.urlencode(post_data))
response = request.read()  
print response 
