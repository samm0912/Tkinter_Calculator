import tkinter as tk
'''Imports Tkinter module
tk is an allias for easy access'''

# Button click handler
def press(v):
    entry.insert(tk.END,v)
    '''Called when a number or operator button is clicked
    Inserts the pressed value at the end of the Entry widget'''
    
def clear():
    entry.delete(0,tk.END)
    '''Clears the Calculator screen
    Delete all characters from index 0 to End'''
# Calculation Function

def back():
    current=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current[:-1])
def calc():
    try:
        result=eval(entry.get())
        '''entry.get() retrives the expression e.g.(2+6)
        eval() evaluates the string as a python expression'''
        
        entry.delete(0,tk.END) #Clears the old expression
        entry.insert(0,result) #Displays exception instead of crashing
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Invalid Expression")
        '''Handles invalid expressionm(e.g 5++)
        Displays "exception" instead of crashing'''
        
#Main window creation
root=tk.Tk() #Creates the main application window

root.title("Calculator")

root.configure(bg="#9f61eb") #Disables resizing of window

root.resizable(False,False) # Disable resizing the windows 

#Entry Widget(Display Screen)
entry=tk.Entry(
    root,
    font=("Times new roman",20),
    bg="#68aeef",
    fg="white",
    bd=0,
    justify="right"
)
'''Text input field
Acts as calculator display
Right-aligned for better claculator look'''

entry.grid(row=0,column=0,columnspan=4,padx=1,pady=12,ipady=10)
 
 #Button Labels
buttons=[
     "7","8","9","/",
     "4","5","6","*",
     "3","2","1","-",
     "0",".","=","+",
 ]
 
'''Represent calculator buttons 
    Stored in list to reduce repetitive code'''
    
#Dynamic Button Creation
r=1
c=0
'''Rows and columms counter for grid layout'''

for b in buttons:
    cmd=calc if b=="=" else lambda x=b: press(x)
    '''If button is "=" call calc()
    else, call press() with the button value 
    lambda x=b prevents late binding issues'''
    
    tk.Button(
        root,
        text=b,
        command=cmd, # these three lines creates a button widget
        font=("Claibri",14),
        width=5,
        height=2,
        bg="#f06ee1",
        fg="white",
        bd=0
    ).grid(row=r,column=c,padx=6,pady=6)
    c+=1
    if c == 4 :
        r+=1
        c=0
        '''moves to next row after 4 buttons'''
# clear button
tk.Button(
    root,
    text="clear",
    command=clear,
    font=("Claibri",14),
    width=5,
    height=2,
    bg="#a3b4f8" if b in "+-*/" else"#3f3f3f",
    fg="white",
    bd=0
).grid(row=r,column=0,columnspan=4,pady=14)
'''Clears the calculator display screen
Spans across all columns'''

tk.Button(
    root,
    text="bkspc",
    command=back,
    font=("Claibri",14),
    width=5,
    height=2,
    bg="#f06ee1",
    fg="white",
    bd=0
).grid(row=r,column=3,padx=6,pady=6)

#Event loop
root.mainloop()
'''Keeps the '''