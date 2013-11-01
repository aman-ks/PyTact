import subprocess as s
import os
import sys
import win
import Recorder 
"""Surprisingly importing Recorder automatically tells the interpreter to execute Recorder.py as if in a function call"""

s.call(["flac","output.wav","-f"]) #This simply changes the file to a .flac to be used by the google speech api
response = win.func('output.flac') #Voila this returns my important response!

index = response.find("utterance")
print response, index  
print response[index+12]
