import sys
from Tkinter import *
import os
import time


def changeLabel():
    global myGui
    time= (v1.get() *3600) + (v2.get() * 60) + v3.get()
    os.system("shutdown /s /t %s " % time)
    myGui.destroy()
    countDown(time)
    

def countDown(number):

    root = Tk()
    root.title("Timer")
    lbl1 = Label()
    lbl1.pack(fill=BOTH, expand=1)
    #countDown(number)
    

    
    lbl1.config(bg='green')
    lbl1.config(height=3, font=('times', 20, 'bold'))
    for k in range(number, 0, -1):
        h=k/3600
        m=(k%3600)/60
        c= (k%3600)%60
        lbl1["text"] = str(h) + " hours " + str(m) + " minutes " + str(c) + " sec"
        root.update()
        time.sleep(1)
    lbl1.config(bg='red')
    lbl1.config(fg='white')
    lbl1["text"] = "Shutting Down"
    root.mainloop()
    
    
 

myGui = Tk()
myGui.geometry('300x200')
myGui.title('Shutdown Timer')

    
hours = StringVar()
hours.set('Set the number of:\n  Hours \nMinutes \nSeconds')

hours1 = Label(myGui, textvariable = hours, height = 4)
hours1.pack()

v1 = IntVar()
v1.set(0)
hoursSet = Entry(myGui, textvariable=v1)
hoursSet.pack()

button1 = Button(myGui, text="Start Timer", width=20, command=changeLabel)
button1.pack(side='bottom', padx=15, pady=15)


v2 = IntVar()
v2.set(0)
minSet = Entry(myGui, textvariable=v2,)
minSet.pack()


v3 = IntVar()
v3.set(0)
secSet = Entry(myGui, textvariable=v3)
secSet.pack()

myGui.mainloop()