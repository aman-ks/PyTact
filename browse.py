import subprocess as s
import os
import sys
import win
import Recorder
import pygame
import time
from pygame.locals import *
#import RPi.GPIO as GPIO
#import raspi 
"""Surprisingly importing Recorder automatically tells the interpreter to execute Recorder.py as if in a function call"""

s.call(["flac","output.wav","-f"]) #This simply changes the file to a .flac to be used by the google speech api
response = win.func('output.flac') #Voila this returns my important response!

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
homo = {
   'HEY' : 'A', 'EH' : 'A',
   'BE' : 'B', 'BEE' : 'B', 'BEA' : 'B',
   'SEE' : 'C', 'SEA' : 'C', 'SI' : 'C',
   'DEE' : 'D',
   'EE':'E','EBAY':'E','EAT':'E' ,
   'EFF' : 'F',
   'GEE' : 'G', 'JI' : 'G',
   'ETCH' : 'H',
   'AYE' : 'I', 'EYE' : 'I',
   'JAY' : 'J',
   'KAY' : 'K', 'CAY' : 'K',
   'YELL' : 'L', 'ELLE' : 'L',
   'EM' : 'M', 'UMM' : 'M', 'UM' : 'M', 'EMM' : 'M',
   'EN' : 'N', 'HEN' : 'N', 'AN' : 'N',
   'OH' : 'O',
   'PEE' : 'P', 'PEA' : 'P',
   'CUE' : 'Q', 'QUEUE' : 'Q', 'QUE' : 'Q',
   'OUR' : 'R', 'HOUR' : 'R', 'ARE' : 'R',
   'ESS' : 'S', 'YES' : 'S', 'ES' : 'S',
   'TEE' : 'T', 'TEA' : 'T',
   'YOU' : 'U',
   'WE' : 'V', 'WEE' : 'V', 'VEE' : 'V',
   'DOUBLE YOU' : 'W', 'DOUBLE' : 'W',
   'EX' : 'X',
   'WHY' : 'Y',
   'ZEE' : 'Z', 'SAID' : 'Z',
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
                  
                  
                  
                  



class LetterMatcher:
        "This class matches the six digit input to a letter and then plays its corresponding sound."
        pygame.init()

        def a(self):
                pygame.mixer.music.load("A.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)

        def b(self):
                pygame.mixer.music.load("B.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def c(self):
                pygame.mixer.music.load("C.mp3")                
                pygame.mixer.music.play()
                time.sleep(3)
        
        def d(self):
                pygame.mixer.music.load("D.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def e(self):
                pygame.mixer.music.load("E.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def f(self):
                pygame.mixer.music.load("F.mp3")                
                pygame.mixer.music.play()
                time.sleep(3)
        
        def g(self):
                pygame.mixer.music.load("G.mp3")                
                pygame.mixer.music.play()
                time.sleep(3)
        
        def h(self):
                pygame.mixer.music.load("H.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def i(self):
                pygame.mixer.music.load("I.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def j(self):
                pygame.mixer.music.load("J.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def k(self):
                pygame.mixer.music.load("K.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def l(self):
                pygame.mixer.music.load("L.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def m(self):
                pygame.mixer.music.load("M.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def n(self):
                pygame.mixer.music.load("N.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def o(self):
                pygame.mixer.music.load("O.mp3")                
                pygame.mixer.music.play()
                time.sleep(3)
        
        def p(self):
                pygame.mixer.music.load("P.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def q(self):
                pygame.mixer.music.load("Q.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def r(self):
                pygame.mixer.music.load("R.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def s(self):
                pygame.mixer.music.load("S.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def t(self):
                pygame.mixer.music.load("T.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def u(self):
                pygame.mixer.music.load("U.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def v(self):
                pygame.mixer.music.load("V.mp3")                
                pygame.mixer.music.play()
                time.sleep(3)
        
        def w(self):
                pygame.mixer.music.load("W.mp3")        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def x(self):
                pygame.mixer.music.load("X.mp3")        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def y(self):
                pygame.mixer.music.load("Y.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def z(self):
                pygame.mixer.music.load("Z.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def zero(self):
                pygame.mixer.music.load("ZERO.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def one(self):
                pygame.mixer.music.load("ONE.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def two(self):
                pygame.mixer.music.load("TWO.mp3")        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def three(self):
                pygame.mixer.music.load("THREE.mp3")                
                pygame.mixer.music.play()
                time.sleep(3)
        
        def four(self):
                pygame.mixer.music.load("FOUR.mp3")                
                pygame.mixer.music.play()
                time.sleep(3)
        
        def five(self):
                pygame.mixer.music.load("FIVE.mp3")                
                pygame.mixer.music.play()
                time.sleep(3)
        
        def six(self):
                pygame.mixer.music.load("SIX.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)
        
        def seven(self):
                pygame.mixer.music.load("SEVEN.mp3")                
                pygame.mixer.music.play()
                time.sleep(3)
        
        def eight(self):
                pygame.mixer.music.load("EIGHT.mp3")                
                pygame.mixer.music.play()
                time.sleep(3)
        
        def nine(self):
                pygame.mixer.music.load("NINE.mp3")                        
                pygame.mixer.music.play()
                time.sleep(3)

        matchSound = {
                                '100000' : a,
                                '101000' : b,         
                                '110000' : c,
                                '110100' : d,
                                '100100' : e,         
                                '111000' : f,
                                '111100' : g,
                                '101100' : h,
                                '011000' : i,
                                '011100' : j,
                                '100010' : k,
                                '101010' : l,
                                '110010' : m,
                                '110110' : n,
                                '100110' : o,
                                '111010' : p,
                                '111110' : q,
                                '101110' : r,
                                '011010' : s,
                                '011110' : t,
                                '100011' : u,
                                '101011' : v,
                                '011101' : w,
                                '110011' : x,
                                '110111' : y,
                                '100111' : z,
                                '000111' : zero,
                                '001000' : one,
                                '001010' : two,
                                '001100' : three,
                                '001101' : four,
                                '001001' : five,
                                '001110' : six,
                                '001111' : seven,
                                '001011' : eight,
                                '000110' : nine
                        }                  

def gpio_call(string):
    
    binary = matchDict[string]
    l = LetterMatcher()
    l.matchSound[binary](l)
    print string,matchDict[string]
    #return matchDict[string]
    #raspi.give_signal_high(matchDict[string]) from the raspi file

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
    pygame.mixer.music.load("sorry.mp3")                
    pygame.mixer.music.play()
    time.sleep(4)
    
    
