import subprocess as s
import os
import sys
import win
import Recorder 
"""Surprisingly importing Recorder automatically tells the interpreter to execute Recorder.py as if in a function call"""

s.call(["flac","output.wav","-f"]) #This simply changes the file to a .flac to be used by the google speech api
response = win.func('output.flac') #Voila this returns my important response!

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','10','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN']
homo = {
  'A' : 'A', 'HEY' : 'A', 'EH' : 'A',
  'B' : 'B', 'BE' : 'B', 'BEE' : 'B', 'BEA' : 'B',
  'C' : 'C', 'SEE' : 'C', 'SEA' : 'C', 'SI' : 'C',
  'D' : 'D', 'DEE' : 'D',
  'E' : 'E',
  'F' : 'F', 'EFF' : 'F',
  'G' : 'G', 'GEE' : 'G', 'JI' : 'G',
  'H' : 'H', 'ETCH' : 'H',
  'I' : 'I', 'AYE' : 'I', 'EYE' : 'I',
  'J' : 'J', 'JAY' : 'J',
  'K' : 'K', 'KAY' : 'K', 'CAY' : 'K',
  'L' : 'L', 'YELL' : 'L', 'ELLE' : 'L',
  'M' : 'M', 'EM' : 'M', 'UMM' : 'M', 'UM' : 'M', 'EMM' : 'M',
  'N' : 'N', 'EN' : 'N', 'HEN' : 'N', 'AN' : 'N',
  'O' : 'O', 'OH' : 'O',
  'P' : 'P', 'PEE' : 'P', 'PEA' : 'P',
  'Q' : 'Q', 'CUE' : 'Q', 'QUEUE' : 'Q', 'QUE' : 'Q',
  'R' : 'R', 'OUR' : 'R', 'HOUR' : 'R', 'ARE' : 'R',
  'S' : 'S', 'ESS' : 'S', 'YES' : 'S', 'ES' : 'S',
  'T' : 'T', 'TEE' : 'T', 'TEA' : 'T',
  'U' : 'U', 'YOU' : 'U',
  'V' : 'V', 'WE' : 'V', 'WEE' : 'V', 'VEE' : 'V',
  'W' : 'W', 'DOUBLE YOU' : 'W', 'DOUBLE' : 'W',
  'X' : 'X', 'EX' : 'X',
  'Y' : 'Y', 'WHY' : 'Y',
  'Z' : 'Z', 'ZEE' : 'Z', 'SAID' : 'Z',
  'ZERO' : 'ZERO', '0' : 'ZERO', 'ZEE ROW' : 'ZERO', 'ZEE ROE' : 'ZERO',
  'ONE' : 'ONE', '1' : 'ONE', 'WON' : 'ONE',
  'TWO' : 'TWO', '2' : 'TWO', 'TO' : 'TWO', 'TOO' : 'TWO',
  'THREE' : 'THREE', '3' : 'THREE', 'TREE' : 'THREE',
  'FOUR' : 'FOUR', '4' : 'FOUR', 'FORE' : 'FOUR', 'FOR' : '4',
  'FIVE' : 'FIVE', '5' : 'FIVE', 'FIE' : 'FIVE',
  'SIX' : 'SIX', '6' : 'SIX', 'SEX' : 'SIX',
  'SEVEN' : 'SEVEN', '7' : 'SEVEN', 'SAVE URN' : 'SEVEN', 'SAVE EARN' : 'SEVEN', 'SAVE UN' : 'SEVEN',
  'EIGHT' : 'EIGHT', '8' : 'EIGHT', 'ATE' : 'EIGHT', 'HATE' : 'EIGHT',
  'NINE' : 'NINE', '9' : 'NINE', 'NIGH IN' : 'NINE' }
#similar_alphabets = {"hey":"a","cue":"q","queue":"q"}
def check_in_alpha(c):
    print "Checking if input is contained in the alphabets list"
    if c in alphabets:
        print True,"Yes ",c,"is a alphabet"
    elif c in homo:
        print True,"Yes I see you meant ",homo[c],"..."      
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
    next_input = next_input.upper()
    print next_input
    check_in_alpha(next_input)
    check_in_numerals(next_input)     
elif index==-1:
    print "Input unclear!"
    
    
    
    
