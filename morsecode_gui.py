
from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
from gpiozero import LED
import time

##SETUP CHANNEL
GPIO.setmode(GPIO.BCM)
#define led port
led = LED(14)
GPIO.setup(14, GPIO.OUT)

    
morseCode = {
    #ALPHABETS
    'A':'.-',
    'B':'-...',
    'C':'-.-.', 
    'D':'-..', 
    'E':'.', 
    'F':'..-.', 
    'G':'--.', 
    'H':'....', 
    'I':'..', 
    'J':'.---', 
    'K':'-.-', 
    'L':'.-..', 
    'M':'--', 
    'N':'-.', 
    'O':'---', 
    'P':'.--.', 
    'Q':'--.-', 
    'R':'.-.', 
    'S':'...',
    'T':'-', 
    'U':'..-', 
    'V':'...-', 
    'W':'.--', 
    'X':'-..-', 
    'Y':'-.--', 
    'Z':'--..', 
    #NUMBERS
    '1':'.----', 
    '2':'..---', 
    '3':'...--', 
    '4':'....-', 
    '5':'.....', 
    '6':'-....', 
    '7':'--...', 
    '8':'---..', 
    '9':'----.', 
    '0':'-----',
    #SIGNS
    '?':'..--..',
    '!':'-.-.--',
    '.':'.-.-.-',
    ',':'--..--',
    ';':'-.-.-.',
    ':':'---...',
    '+':'.-.-.',
    '-':'-....-',
    '/':'-..-.',
    '=':'-...-'
}

#GUI definitions
mygui = Tk()
mygui.title("Morse code Tkinter")
myFont = tkinter.font.Font(family = 'Comic Sans', size = 12, weight = "bold")

#converting morse code to GPIO dictionary
morseCodeGpio= {
   '.': 'dot(), ', 
   '-': 'dash(), '
}

#entry point widget to show where to enter text
entryPoint = Button(mygui, text = "write here: ")
entryPoint.pack()
#where text will be entered
userInput = Entry(mygui, width = 12)
userInput.pack(side = 'top')

#define dot function 
def dot():
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
#define line function 
def line():
    led.on()
    time.sleep(2)
    led.off()
    time.sleep(2)

def converter():
    input = userInput.get()
    input = input.upper()
    length = len(value)
    if(length <= 12):
        for i in range(length):
            for char in morseCode[input[i]]:
                if char == '-':
                    line()
                elif char == '.':
                    dot()
    elif(length > 12):
        error = entryPoint(text = "max limit of 12 characters")
        error.grid(row =1, column = 0)
           
#defining the close function
def Close():
    mygui.destroy()
    GPIO.cleanup()
    print("closing window")

#translate button
translateButton = Button(mygui, text = 'Translate', font = myFont, command = converter, bg = 'white', height = 2, width = 10)
translateButton.pack(side = 'right')

#exit button 
Off = Button(mygui, text = "exit", font = myFont, command = Close, bg = "white", height = 1, width = 15)
Off.pack(side = 'bottom')
mygui.mainloop()
