
#making a GUI
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#hardware
redLed = LED(14)
greenLed = LED(15)
blueLed = LED(18)

#define every function
def RedLed():
    if redLed.is_lit:
        redLed.off()
        Rled["text"] = "turn led on"
    else:
        redLed.on()
        greenLed.off()
        blueLed.off()
        Rled["text"] = "turn led off"
    
def GreenLed():
    if greenLed.is_lit:
        greenLed.off()
        Gled["text"] = "turn led on"
    else:
        greenLed.on()
        redLed.off()
        blueLed.off()
        Gled["text"] = "turn led off"
    
def BlueLed():
    if blueLed.is_lit:
        blueLed.off()
        Bled["text"] = "turn led on"
    else:
        blueLed.on()
        redLed.off()
        greenLed.off()
        Bled["text"] = "turn led off"

def Close():
    mygui.destroy()

#GUI definitions
mygui = Tk()
mygui.title("LED Toggler for 3 lights")
myFont = tkinter.font.Font(family = 'Comic Sans', size = 12, weight = "bold")
#myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

##creating radiobuttons
Rled = Radiobutton(mygui, text = "turn red led on",font = myFont, value = 0, command = RedLed, bg = "red", height = 4, width = 40)
Rled.grid(row=0, column=1)

Gled = Radiobutton(mygui, text = "turn green led on", font = myFont, value = 1, command = GreenLed, bg = "green", height = 4, width = 40)
Gled.grid(row=1, column=1)

Bled = Radiobutton(mygui, text = "turn blue led on",font = myFont, value = 2, command = BlueLed, bg = "blue", height = 4, width = 40)
Bled.grid(row=2, column=1)

Off = Button(mygui, text = "exit", font = myFont, command = Close, bg = "white", height = 4, width = 40)
Off.grid(row=3, column=1)

mygui.mainloop()
