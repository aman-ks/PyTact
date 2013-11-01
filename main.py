import subprocess as s
import os
import sys
import win
import Recorder 
"""Surprisingly importing Recorder automatically tells the interpreter to execute Recorder.py as if in a function call"""

s.call(["flac","output.wav","-f"]) #This simply changes the file to a .flac to be used by the google speech api
response = win.func('output.flac') #Voila this returns my important response!

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','10','one','two','three','four','five','six','seven','eight','nine','ten']
def check_in_alpha(c):
    print "Checking if input is contained in the alphabets list"
    if c in alphabets:
        print True,"Yes ",c,"is a alphabet"
    else:
        print "The string",c,"is probably a word!"

def check_in_numerals(c):
    print "Checking if input is contained in the numbers list"
    if c in numbers:
        print True,"Yes ",c," a number"
    else:
        print "The string ",c," is probably a word!"

index = response.find("utterance")
if index!=-1:
    print response, index
    index = index + 12  
    index2 = response.find(",",index)
    index2 = index2 - 1
    print index, index2
    next_input = response[index:index2]
    next_input = next_input.lower()
    print next_input
    check_in_alpha(next_input)
    check_in_numerals(next_input)     
elif index==-1:
    print "Input unclear!"
