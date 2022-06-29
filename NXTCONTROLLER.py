import tkinter as tk
import nxt.locator
import nxt.motor
from usb.core import NoBackendError

window = tk.Tk()

window.configure(background='black')
window.geometry('600x500')

label = tk.Label(window, text="WELCOME TO The NXT CONTROLLER - DESIGN T - A", pady=5, padx=5, font=9, bg="black",
                 fg="white")
label.pack()

b = None
# Handling keypress events



KeyPress
def KeyPress(event):
    print(event.char)
    if (event.char == "s"):
        Bot()
    if (event.char == "z"):
        Top()
    if (event.char == "d"):
        Right()
    if (event.char == "q"):
        Left()

def KeyRelease(event):
    if (event.char == "s"):
        print('down movement')
    if (event.char == "z"):
        print("top movement")
    if (event.char == "d"):
        print("right movement")
    if (event.char == "q"):
        print("left movement")


def ConnectTheBrick():
    global b
    StatusModifier(0)
    try:

        b = nxt.locator.find(host="NXT's MAC ADDR HERE" )
        StatusModifier(2)
        MotorInit()  # initialise motor behavior

    except(NoBackendError):  # in case bluetooth/usb error occures
        StatusModifier(1)
        print("backenderror")

    except():
        StatusModifier(1)


def StatusModifier(StatID):
    if StatID == 0 :
        StatMsg = "Status : Connecting"
        StatusLabel.config(text=StatMsg, fg="blue"
                                            "")
    if StatID == 1:
        StatMsg = "Status : Unable to connect to NXT"
        StatusLabel.config(text=StatMsg, fg="red")

    if StatID == 2:
        StatMsg = "Status : Connected"
        StatusLabel.config(text=StatMsg, fg="green")

    if StatID == 3:
        StatMsg = "Status : Connect the Nxt First"
        StatusLabel.config(text=StatMsg, fg="yellow")

    if StatID == 4:
        StatMsg = "Status : Motor Running"
        StatusLabel.config(text=StatMsg, fg="orange")

    if StatID == 5 : 
        StatMsg = "Status : Nxt not connecting"
        StatusLabel.config(text=StatMsg, fg="red")

def Top():
    if b != None:
        StatusModifier(4)

        both.run(-80, 360)
        StatusModifier(2)
    else:
        StatusModifier(3)

def Bot():
    if b != None:
        StatusModifier(4)
        both.run(80, 360)
        StatusModifier(2)
    else:
        StatusModifier(3)


def Left():
    if b != None:
        StatusModifier(4)
        Rotation.run(-80, 360)
        StatusModifier(2)
    else:
        StatusModifier(3)


def Right():
    if b != None:
        StatusModifier(4)
        Rotation.run(80, 360)
        StatusModifier(2)
    else:
        StatusModifier(3)


both = None
Rotation = None
UpMotor = None
DownMotor = None



def MotorInit():
    try:
        global both
        global Rotation

        UpMotor = b.get_motor(nxt.motor.Port.A)
        DownMotor = b.get_motor(nxt.motor.Port.C)
        both = nxt.motor.SynchronizedMotors(UpMotor, DownMotor, 0)
        Rotation = nxt.motor.SynchronizedMotors(UpMotor, DownMotor, 90)
        leftboth = nxt.motor.SynchronizedMotors(UpMotor, DownMotor, 100)
        rightboth = nxt.motor.SynchronizedMotors(UpMotor, DownMotor, 100)

    except:
        StatusModifier(3)


StatusLabel = tk.Label(window, text="Status : ", pady=10, padx=10, font=9, bg="black", fg="white")
StatusLabel.config(font=('Helvatical', 13))

ConnectNXT = tk.Button(window, text="Connect", padx=10, pady=10, bg="black", fg='white', command=ConnectTheBrick)

TopButton = tk.Button(window, text="UP", padx=10, pady=10, bg="black", fg='white', height=1, width=5, command=Top)
LeftButton = tk.Button(window, text="LEFT", padx=10, pady=10, bg="black", fg='white', height=1, width=5, command=Left)
RightButton = tk.Button(window, text="RIGHT", padx=10, pady=10, bg="black", fg='white', height=1, width=5,command=Right)
BotButton = tk.Button(window, text="DOWN", padx=10, pady=10, bg="black", fg='white', height=1, width=5, command=Bot)

# Place buttons
StatusLabel.place(x=1, y=50)
ConnectNXT.place(x=499, y=50)
TopButton.place(x=300, y=100)
BotButton.place(x=300, y=200)
RightButton.place(x=350, y=150)
LeftButton.place(x=250, y=150)


# Pack the buttons into the GUI


window.bind("<KeyPress>", KeyPress)
window.bind("<KeyRelease>", KeyRelease)

label.pack()

window.mainloop()
