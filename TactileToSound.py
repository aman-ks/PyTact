import pygame
import time
import sys
from pygame.locals import *
from pygsr import Pygsr


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

	matchDict = {
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
	
	def matcher(self):
		but = raw_input("Please enter numerical braille code.\n")
		self.matchDict[but](self)
		

class Colours:
	"This class lists RGB values of colours."
	
	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	darkBlue = (0, 0, 128)
	white = (255, 255, 255)
	black = (0, 0, 0)
	pink = (255, 200, 200)
	grey = (128, 128, 128)

class GUILol():
	"This makes a GUI to test PyTact. Lol -_-"
	
	def __init__(self):
		
		pygame.init()
		
		screen = pygame.display.set_mode((300, 500))
		pygame.display.set_caption('PyTact Tester')
		screen.fill(Colours.white)
		

		while True:	
			pygame.display.update()
			for event in pygame.event.get():		
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

class Listener():
    """"Listens and converts to text."""
    
    def __init__(self):
        pass
        
    def listen(self):
        speech = Pygsr()
        speech.record(2)
        phrase, complete_response = speech.speech_to_text('en_IN')
        print phrase
        
class Another():
    """Another convertor. Text to 6 digit."""
    
    def __init__(self, text):
       self.text = '1234' 
                

       self.matchDict2 = {
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
                    'ZERO' : '000111', 
                    'ONE' : '001000', 
                    'TWO' : '001010', 
                    'THREE' : '001100', 
                    'FOUR' : '001101', 
                    'FIVE' : '001001', 
                    'SIX' : '001110', 
                    'SEVEN' : '001111', 
                    'EIGHT' : '001011', 
                    'NINE' : '000110'
                  }

    #def generator(self):
        











#play = LetterMatcher()
#play.matcher()
#GUI = GUILol()


hear = Listener()
hear.listen()
