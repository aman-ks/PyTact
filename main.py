import subprocess as s
import os
import sys
import win
import Recorder 
"""Surprisingly importing Recorder automatically tells the interpreter to execute Recorder.py as if in a function call"""

s.call(["flac","output.wav","-f"]) #This simply changes the file to a .flac to be used by the google speech api
response = win.func('output.flac') #Voila this returns my important response!

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
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
  'ZERO' : '0', 'ZEE ROW' : '0', 'ZEE ROE' : '0',
  'ONE' : '1','WON' : '1',
  'TWO' : '2', '2' : 'TWO', 'TO' : '2', 'TOO' : '2','TUBE':'2',
  'THREE' : '3','TREE' : '3',
  'FOUR' : '4','FORE' : '4', 'FOR' : '4','FULL':'4',
  'FIVE' : '5','FIE' : '5',
  'SIX' : '6','SEX' : '6',
  'SEVEN' : '7','SAVE URN' : '7', 'SAVE EARN' : '7', 'SAVE UN' : '7',
  'EIGHT' : '8','ATE' : '8', 'HATE' : '8','ATT':'8',
  'NINE' : '9','NIGH IN' : '9' }
#similar_alphabets = {"hey":"a","cue":"q","queue":"q"}


#match to braille output - GPIO pins
matchDict = {
                    'A' : '100000', 
                    'B' : '101000', 
                    'C' : '110000', 
                    'D' : '110100', 
                    'E' : '100100', 
                    'F' : '111000', 
                    'G' : '111100', 
                    'H' : '101100', 
                    'I' : '011000', 
                    'J' : '011100', 
                    'K' : '100010', 
                    'L' : '101010', 
                    'M' : '110010', 
                    'N' : '110110', 
                    'O' : '100110', 
                    'P' : '111010', 
                    'Q' : '111110', 
                    'R' : '101110', 
                    'S' : '011010', 
                    'T' : '011110', 
                    'U' : '100011', 
                    'V' : '101011', 
                    'W' : '011101', 
                    'X' : '110011', 
                    'Y' : '110111', 
                    'Z' : '100111', 
                    '0' : '000111', 
                    '1' : '001000', 
                    '2' : '001010', 
                    '3' : '001100', 
                    '4' : '001101', 
                    '5' : '001001', 
                    '6' : '001110', 
                    '7' : '001111', 
                    '8' : '001011', 
                    '9' : '000110'
                  }

def gpio_call(string):
    print string,matchDict[string]
    #return matchDict[string]


def check_in_alpha(c):
    print "Checking if input is contained in the alphabets list"
    if c in alphabets:
        print True,"Yes ",c,"is a alphabet"
        gpio_call(c)
        return True
    elif c in homo:
        print True,"Yes I see you meant ",homo[c],"..."
        gpio_call(homo[c])
        return True      
    else:
        print "The string",c,"is probably a word!"
        return False

def check_in_numerals(c):
    print "Checking if input is contained in the numbers list"
    if c in numbers:
        print True,"Yes ",c," a number"
        gpio_call(c)
        return True
    else:
        print "The string ",c," is probably a word or an alphabet!"
        return False
        
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
    if(check_in_numerals(next_input)==False):
        check_in_alpha(next_input)     
elif index==-1:
    print "Input unclear!"
    
    
    
    
