import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
from pimoroni import RGBLED
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)

display.set_backlight(0.5)
display.set_font("bitmap8")

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)
shape = 0


def msts():
    msts = ""
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()
    



clear()

clear()
display.set_pen(GREEN)
display.text("InspireOS", 10, 70, 240, 4)
display.set_pen(WHITE)
display.text("Starting, Please wait.", 10, 105, 240, 2)
display.update()
time.sleep(3)
boot = 1
programs = ["System Info", "Demo App"]
buildnum = 5
buildnumverify = 5
bootcount =+ 1
builddate = "June 29, 2024"
sysreg = ["buildnum:", buildnum, "bootcount:", bootcount, "buildnumverify:", buildnumverify, "build_date:", builddate, "-"]



if boot == 1:
    clear()
display.set_pen(CYAN)
display.text("InspireOS Beta", 10, 10, 240, 4)
display.set_pen(WHITE)
display.text("Press A for menu", 10, 80, 240, 2)
display.update()
time.sleep(0.1)
while True:
    if button_a.read():                                  
        mode = 1
        msts = 1
        clear()                                           
        display.set_pen(WHITE)                           
        display.text("Menu", 10, 10, 240, 4)
        display.text("Press Y to scroll", 15, 45, 240, 2)
        display.text("Demo App", 15, 60, 240 , 2)
        display.text("System Info", 15, 75, 240, 2)
        display.rectangle(7, 45, 7, 10)
        appsel = 1
        display.update()
    time.sleep(0.1)
    if button_y.read() and appsel == 1 and msts == 1:
        if mode == 1:
            clear()                                           
            display.set_pen(WHITE)                           
            display.text("Menu", 10, 10, 240, 4)
            display.text("Press Y to scroll", 15, 45, 240, 2)
            display.text("Demo App", 15, 60, 240 , 2)
            display.text("System Info", 15, 75, 240, 2)
            display.rectangle(7, 63, 7, 10)
            appsel = 2
            display.update()                                 
            time.sleep(1)         
            shape = 1
        while True:
            if shape == 1:
                 clear()                                           
            display.set_pen(WHITE)                           
            display.text("Menu", 10, 10, 240, 4)
            display.text("Press Y to scroll", 15, 45, 240, 2)
            display.text("Demo App", 15, 60, 240 , 2)
            display.text("System Info", 15, 75, 240, 2)
            display.rectangle(7, 63, 7, 10)
            rectanglestatus = "DRAWN"
            display.update()                                 
            time.sleep(1)         
            msts = 2
            shape = 1
            mode = 1
            if button_x.read() and appsel == 2:
                clear()
                display.text("Welcome to the demo app!", 10, 80, 240, 2)
                display.update()
                time.sleep(1)
                display.text("This is a test app for InspireOS", 10, 80, 240, 2)
                display.update()
                time.sleep(1)
                display.text("The demo will play in a second.", 10, 80, 240, 2)
                display.update()
                time.sleep(1)
                display.text("Sample Text", 10, 80, 240, 4)
                display.update()
                time.sleep(1)
                display.set_pen(GREEN)
                display.rectangle(10, 80, 240, 100)
                display.update()
                time.sleep(1)
                display.text(":D", 10, 80, 240, 2)
                display.update()
                time.sleep(1)
                display.set_pen(CYAN)
                display.text(":D", 10, 80, 240, 2)
                display.update()
                time.sleep(1)
                clear()
                display.text("InspireOS", 10, 80, 240, 4)
                display.update()
                time.sleep(1)
                display.set_pen(MAGENTA)
                display.text("InspireOS", 10, 80, 240, 4)
                display.update()
                time.sleep(1)
                clear()
                deastat = "done"
                display.set_pen(WHITE)
                #app script end
    if msts == 2 and button_y.read():
        if mode == 1:
            clear()                                           
            display.set_pen(WHITE)                           
            display.text("Menu", 10, 10, 240, 4)
            display.text("Press Y to scroll", 15, 45, 240, 2)
            display.text("Demo App", 15, 60, 240 , 2)
            display.text("System Info", 15, 75, 240, 2)
            display.rectangle(7, 75, 7, 10)
            appsel = 2
            display.update()                                 
            time.sleep(1)         
            shape = 1
        while True:
            if shape == 1:
                 clear()                                           
            display.set_pen(WHITE)                           
            display.text("Menu", 10, 10, 240, 4)
            display.text("Press Y to scroll", 15, 45, 240, 2)
            display.text("Demo App", 15, 60, 240 , 2)
            display.rectangle(7, 75, 7, 10)
            rectanglestatus = "DRAWN"
            display.update()                                 
            time.sleep(1)         
            msts = 2
            shape = 1
            mode = 1
            if msts == 2 and appsel == 2 and button_x.read():
                clear()
                display.text("System Info", 10, 10, 240, 4)
                display.text("Raspberry Pi Pico", 15, 45, 240, 2)
                display.text("RP2040", 15, 60, 240, 2)
                display.text("OS: InspireOS Beta", 15, 75, 240, 2)
                display.text("OS Build: Beta 1, Build 7", 15, 90, 240, 2)
                time.sleep(2)
if deastat == "done":
   while True:
     display.text("InspireOS Beta 1", 10, 10, 240, 4)
     display.text("Press A for menu", 10, 80, 240, 2)
     display.update()
     time.sleep(0.1)
while True:
    if button_a.read():                                  
        mode = 1
        msts = 1
        clear()                                           
        display.set_pen(WHITE)                           
        display.text("Menu", 10, 10, 240, 4)
        display.text("Press Y to scroll", 15, 45, 240, 2)
        display.text("Demo App", 15, 60, 240 , 2)
        display.text("System Info", 15, 75, 240, 2)
        display.rectangle(7, 45, 7, 10)
        appsel = 1
        display.update()
    time.sleep(0.1)
    if button_y.read() and appsel == 1 and msts == 1:
        if mode == 1:
            clear()                                           
            display.set_pen(WHITE)                           
            display.text("Menu", 10, 10, 240, 4)
            display.text("Press Y to scroll", 15, 45, 240, 2)
            display.text("Demo App", 15, 60, 240 , 2)
            display.text("System Info", 15, 75, 240, 2)
            display.rectangle(7, 63, 7, 10)
            appsel = 2
            display.update()                                 
            time.sleep(1)         
            shape = 1
        while True:
            if shape == 1:
                 clear()                                           
            display.set_pen(WHITE)                           
            display.text("Menu", 10, 10, 240, 4)
            display.text("Press Y to scroll", 15, 45, 240, 2)
            display.text("Demo App", 15, 60, 240 , 2)
            display.rectangle(7, 63, 7, 10)
            rectanglestatus = "DRAWN"
            display.update()                                 
            time.sleep(1)         
            msts = 2
            shape = 1
            mode = 1
