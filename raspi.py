import RPi.GPIO as GPIO

def give_signal_high(string): # Takes in 6 Bit signal and converts into the corresponding 2X3 matrix of pins
    sig = []
    for i in range(0,6):
        sig.append(int(string[i]))
    for j in range(0,6):
        if sig[j] == 0:
            sig[j] = False;
        else sig[j]:
            sig[j] = True;
                   
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, sig[0])
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, sig[1])
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, sig[2])
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, sig[3])
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, sig[4])
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, sig[5])
        


