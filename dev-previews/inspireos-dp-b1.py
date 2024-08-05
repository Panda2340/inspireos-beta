import time

def clear():
    print("\n" * 50)

def display_text(text, x, y, size):
    print(f"Display at ({x}, {y}): {text}")

def simulate_button_press(button_name):
    return input(f"Press {button_name} button: ").strip().lower() == 'y'

clear()
display_text("InspireOS", 10, 70, 4)
display_text("Starting, Please wait.", 10, 105, 2)
time.sleep(3)

boot = 1
programs = ["System Info", "Demo App"]
buildnum = 5
buildnumverify = 5
bootcount = 1
builddate = "June 29, 2024"
day = 1
month = 1
year = 2024
currentdate = f"{month}-{day}-{year}"
hour = 0
minute = 0
time_str = f"{hour:02}:{minute:02}"
sysreg = [
    f"buildnum: {buildnum}",
    f"bootcount: {bootcount}",
    f"buildnumverify: {buildnumverify}",
    f"build_date: {builddate}",
    f"currentdate: {currentdate}",
    f"time: {time_str}"
]

if boot == 1:
    clear()
    display_text("InspireOS Beta", 10, 10, 4)
    display_text("Press A for menu", 10, 80, 2)
    time.sleep(0.1)

mode = 1
msts = 1
appsel = 1
shape = 0

while True:
    if simulate_button_press('A'):
        mode = 1
        msts = 1
        clear()
        display_text("Menu", 10, 10, 4)
        display_text("Press Y to scroll", 15, 45, 2)
        display_text("Demo App", 15, 60, 2)
        display_text("System Info", 15, 75, 2)
        appsel = 1
        time.sleep(0.1)
    if simulate_button_press('Y') and appsel == 1 and msts == 1:
        clear()
        display_text("Menu", 10, 10, 4)
        display_text("Press Y to scroll", 15, 45, 2)
        display_text("Demo App", 15, 60, 2)
        display_text("System Info", 15, 75, 2)
        appsel = 2
        shape = 1
        time.sleep(1)
    if shape == 1:
        clear()
        display_text("Menu", 10, 10, 4)
        display_text("Press Y to scroll", 15, 45, 2)
        display_text("Demo App", 15, 60, 2)
        display_text("System Info", 15, 75, 2)
        time.sleep(1)
        msts = 2
        mode = 1
        if simulate_button_press('X') and appsel == 2:
            clear()
            display_text("Welcome to the demo app!", 10, 80, 2)
            time.sleep(1)
            display_text("This is a test app for InspireOS", 10, 80, 2)
            time.sleep(1)
            display_text("The demo will play in a second.", 10, 80, 2)
            time.sleep(1)
            display_text("Sample Text", 10, 80, 4)
            time.sleep(1)
            display_text(":D", 10, 80, 2)
            time.sleep(1)
            clear()
            display_text("InspireOS", 10, 80, 4)
            time.sleep(1)
    if msts == 2 and simulate_button_press('Y'):
        clear()
        display_text("Menu", 10, 10, 4)
        display_text("Press Y to scroll", 15, 45, 2)
        display_text("Demo App", 15, 60, 2)
        display_text("System Info", 15, 75, 2)
        time.sleep(1)
        shape = 1
        mode = 1
    if msts == 2 and appsel == 2 and simulate_button_press('X'):
        clear()
        display_text("System Info", 10, 10, 4)
        display_text("Raspberry Pi Pico", 15, 45, 2)
        display_text("RP2040", 15, 60, 2)
        display_text("OS: InspireOS Beta", 15, 75, 2)
        display_text("OS Build: Beta 1, Build 7", 15, 90, 2)
        time.sleep(2)
    if msts == 2:
        while True:
            display_text("InspireOS Beta 1", 10, 10, 4)
            display_text("Press A for menu", 10, 80, 2)
            time.sleep(0.1)
