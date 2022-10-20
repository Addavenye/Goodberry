#Import all from tkinter
# to this program
from tkinter import *
 
# Declare global variable
window = None

counter = 0
scounter = 0
tcounter = 0
fcounter = 0
vcounter = 0
total = 0
# Define a function for starting the counter

def update():
    global counter
    global scounter
    global tcounter
    global fcounter
    global vcounter
    global total

    total = counter+scounter+tcounter+fcounter+vcounter
    totallabel = Label(window, fg = 'white', bg = 'green')
    totallabel.grid(row = 3, column = 6)
    totallabel.config(text = str(total*10))
    thlabel = Label(window, fg = 'white', bg = 'green')
    thlabel.grid(row = 4, column = 6)
    thlabel.config(text = str('Goodberrys'))
    window.after(100, update) # run itself again after 1000 ms

def total() :
    global total
    


def start() :
 
    global counter
 
    counterLabel = Label(window, fg = 'white', bg = 'green')

    counterLabel.grid(row = 3, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    counter += 1
    counterLabel.config(text = str(counter))
    val = statusField.get()
    if val == "Stop" :
        counterLabel.destroy()
        statusField.delete(0,"end")
        counter -= 1

def stop() :
 
    global counter
 
    counterLabel = Label(window, fg = 'white',
                         bg = 'green')

    counterLabel.grid(row = 3, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    counter -= 1
    counterLabel.config(text = str(counter))
    val = statusField.get()
    if val == "Stop" :
        counterLabel.destroy()
        statusField.delete(0,"end")
        counter -= 1
 
 
def reset() :
 
    global counter ,scounter, tcounter, fcounter, vcounter
 
    counterLabel = Label(window, text = str(counter),
                   fg = 'black', bg = 'green')
    counterLabel.grid(row = 2, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
 
def sstart() :
 
    global scounter
 
    scounterLabel = Label(window, fg = 'white', bg = 'green')

    scounterLabel.grid(row = 6, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    scounter += 1
    scounterLabel.config(text = str(scounter))
    val = statusField.get()
    if val == "Stop" :
        scounterLabel.destroy()
        statusField.delete(0,"end")
        scounter -= 1

def sstop() :
 
    global scounter
 
    scounterLabel = Label(window, fg = 'white',
                         bg = 'green')

    scounterLabel.grid(row = 6, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    scounter -= 1
    scounterLabel.config(text = str(scounter))
    val = statusField.get()
    if val == "Stop" :
        scounterLabel.destroy()
        statusField.delete(0,"end")
        scounter -= 1
        
def tstart():
    
     global tcounter
     
     tcounterLabel = Label(window, fg = 'white',bg = 'green')

     tcounterLabel.grid(row = 9, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
     tcounter += 1
     tcounterLabel.config(text = str(tcounter))
     val = statusField.get()
     if val == "Stop" :
         tcounterLabel.destroy()
         statusField.delete(0,"end")
         tcounter -= 1

def tstop() :
 
    global tcounter
 
    tcounterLabel = Label(window, fg = 'white',
                         bg = 'green')

    tcounterLabel.grid(row = 9, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    tcounter -= 1
    tcounterLabel.config(text = str(tcounter))
    val = statusField.get()
    if val == "Stop" :
        tcounterLabel.destroy()
        statusField.delete(0,"end")
        tcounter -= 1

def fstart() :

    global fcounter
     
    fcounterLabel = Label(window, fg = 'white',bg = 'green')

    fcounterLabel.grid(row = 12, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
    fcounter += 1
    fcounterLabel.config(text = int(fcounter))
    val = statusField.get()
    if val == "Stop" :
         fcounterLabel.destroy()
         statusField.delete(0,"end")
         fcounter -= 1

def fstop() :
 
    global fcounter
 
    fcounterLabel = Label(window, fg = 'white',
                         bg = 'green')

    fcounterLabel.grid(row = 12, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    fcounter -= 1
    fcounterLabel.config(text = int(fcounter))
    val = statusField.get()
    if val == "Stop" :
        fcounterLabel.destroy()
        statusField.delete(0,"end")
        fcounter -= 1
        
def vstart() :

    global vcounter
     
    vcounterLabel = Label(window, fg = 'white',bg = 'green')

    vcounterLabel.grid(row = 15, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
    vcounter += 1
    vcounterLabel.config(text = int(vcounter))
    val = statusField.get()
    if val == "Stop" :
         vcounterLabel.destroy()
         statusField.delete(0,"end")
         vcounter -= 1

def vstop() :
 
    global vcounter
 
    vcounterLabel = Label(window, fg = 'white',
                         bg = 'green')

    vcounterLabel.grid(row = 15, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    vcounter -= 1
    vcounterLabel.config(text = int(vcounter))
    val = statusField.get()
    if val == "Stop" :
        vcounterLabel.destroy()
        statusField.delete(0,"end")
        vcounter -= 1
# Main code
if __name__ == "__main__" :
     
    # Create a window container
    window = Tk()
    window.configure(background = 'lime')
    # Set the title of window container
    window.title("Goodberry counter")
    #label
    var = StringVar()
    tlabel=Label(window, textvariable=var, fg='black', bg = 'Grey')
    var.set("Goodberry")
    tlabel.grid(row = 1, column = 2, padx = "15", pady = "15")
    #level 1
    var = StringVar()
    Llabel=Label(window, textvariable=var, fg='black', bg = 'green')
    var.set("level 1")
    Llabel.grid(row = 2, column = 2, padx = "15", pady = "15")
    
    # Create a label using Label() widget
    counterLabel = Label(window, text = str(counter),
                   fg = 'black', bg = 'lime')
    # Placing the widgets at respective
    # positions in table like structure
    # using grid() method
   
    counterLabel.grid(row = 3, column = 2, padx = "15", pady = "15")
 
    # Create a Button and attached 
    # function using Button() widget
    startButton = Button(window, text = "+1",
                    bg = "red", fg = "black",
                    command = start)
 
    startButton.grid(row = 3, column = 3,
                     ipadx = "15", ipady = "15",
                    padx = "15", pady = "15")
 
    # Create a Button and attached 
    # function using Button() widget
    stopButton = Button(window, text = "-1",
                    bg = "red", fg = "black",
                    command = stop)
 
    # Place button widget in grid at (3, 2)
    stopButton.grid(row = 3, column = 1,
                     ipadx = "15", ipady = "15",
                    padx = "15", pady = "15")

##     #level 2
    var = StringVar()
    Slabel=Label(window, textvariable=var, fg='black', bg = 'green')
    var.set("level 2")
    Slabel.grid(row = 5, column = 2, padx = "15", pady = "15")
    Slabel.grid(row = 5, column = 2, padx = "15", pady = "15")
 
    startButton = Button(window, text = "+1",
                    bg = "red", fg = "black",
                    command = sstart)
 
    startButton.grid(row = 6, column = 3,
                     ipadx = "15", ipady = "15",
                    padx = "15", pady = "15")

    stopButton = Button(window, text = "-1",
                    bg = "red", fg = "black",
                    command = sstop)

    stopButton.grid(row = 6, column = 1,
                     ipadx = "15", ipady = "15",
                    padx = "15", pady = "15")
##    #level 3
    var = StringVar()
    tlabel=Label(window, textvariable=var, fg='black', bg = 'green')
    var.set("level 3")
    tlabel.grid(row = 8, column = 2, padx = "15", pady = "15")
    tlabel.grid(row = 8, column = 2, padx = "15", pady = "15")
 
    startButton = Button(window, text = "+1",
                    bg = "red", fg = "black",
                    command = tstart)
 
    startButton.grid(row = 9, column = 3,
                     ipadx = "15", ipady = "15",
                    padx = "15", pady = "15")

    stopButton = Button(window, text = "-1",
                    bg = "red", fg = "black",
                    command = tstop)

    stopButton.grid(row = 9, column = 1,
                     ipadx = "15", ipady = "15",
                    padx = "15", pady = "15")
  
##  level 4
    var = StringVar()
    flabel=Label(window, textvariable=var, fg='black', bg = 'green')
    var.set("level 4")
    flabel.grid(row = 11, column = 2, padx = "15", pady = "15")
    flabel.grid(row = 11, column = 2, padx = "15", pady = "15")
 
    fstartButton = Button(window, text = "+1",
                    bg = "red", fg = "black",
                    command = fstart)
 
    fstartButton.grid(row = 12, column = 3,
                     ipadx = "15", ipady = "15",
                    padx = "15", pady = "15")

    fstopButton = Button(window, text = "-1",
                    bg = "red", fg = "black",
                    command = fstop)

    fstopButton.grid(row = 12, column = 1,
                     ipadx = "15", ipady = "15",
                    padx = "15", pady = "15")
##  level 5
    var = StringVar()
    vlabel=Label(window, textvariable=var, fg='black', bg = 'green')
    var.set("level 5")
    vlabel.grid(row = 14, column = 2, padx = "15", pady = "15")
    vlabel.grid(row = 14, column = 2, padx = "15", pady = "15")
 
    vstartButton = Button(window, text = "+1",
                    bg = "red", fg = "black",
                    command = vstart)
 
    vstartButton.grid(row = 15, column = 3,
                     ipadx = "15", ipady = "15",
                    padx = "15", pady = "15")

    vstopButton = Button(window, text = "-1",
                    bg = "red", fg = "black",
                    command = vstop)

    vstopButton.grid(row = 15, column = 1,
                     ipadx = "15", ipady = "15",
                    padx = "15", pady = "15")

    # we will not attach this widget to the window
    # because we don't want to place it
    # this is used for only stoping and starting
    # the counter as a flag
     
    # Create text entry box for : status field
    statusField = Entry(window)
    # Start the window,
    # waiting for events and
    # updating the GUI.
    update()
    window.mainloop()
