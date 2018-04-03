#program that converts miles to kilometers
import logging
from tkinter import *
from tkinter import Tk, ttk, messagebox

#creating logging
logging.basicConfig(filename="length.log", level=logging.INFO)

#create window object

window = Tk()
window.title("Length Converter")
window.configure(background="Black")

# #define the program frame
# Tops = Frame(window, width=500, height=400, relief="raise")
# Tops.pack(side=TOP)
# LeftMainFrame = Frame(window, width=300, height=300, bd=8, relief="raise")
# LeftMainFrame.pack(side=LEFT)
# RightMainFrame = Frame(window, width=300, height=300, bd=8, relief="raise")
# RightMainFrame.pack(side=RIGHT)

#define variables
value0 = StringVar()
convert = DoubleVar()
Distance = DoubleVar()


#Define convertion
def ConDistance():
    if value0.get() == "Miles to Kilometers":
        convert1 = float(convert.get() * 1.609344)
        convert2 = str("%.1f"%(convert1)), 'Kilometers'
        Distance.set(convert2)
    elif value0.get() == "Kilometers to Miles":
        convert1 = float(convert.get() / 1.609344)
        convert2 = str("%.1f"%(convert1)), 'Miles'
        Distance.set(convert2)
    elif (value0.get() == "") or (Distance.set(0.0)):
        messagebox.showinfo("Make a conversion selection")



#define combobox
box = ttk.Combobox(textvariable=value0, state="read only", width=29)
box["values"] = ("", "Miles to Kilometers", "Kilometers to Miles")
box.current(0)
box.grid(row=0, column=2)

#define entries
e1 = Entry(textvariable=convert, bd=2, width=30, justify='center').grid(row=2, column=2)
d1 = Label(textvariable=Distance, bd=2, width=30, bg='white', pady=2, padx=2, relief="sunken").grid(row=4, column=2)
s1 = Label(bd=2, width=30, pady=2, padx=2, relief="sunken").grid(row=6, column=2)


#Exit and Reset function
def qExit():
    qExit = messagebox.askyesno("Exit System", "Do you want to quit?")
    if qExit > 0:
        window.destroy()
        return


def Reset():
    value0.set("")
    convert.set("0.0")
    Distance.set("0.0")


#define buttons
b1 = Button(text="Convert", width=10, command=ConDistance).grid(row=2, column=6)
b2 = Button(text="Reset", width=10, command=Reset).grid(row=4, column=6)
b3 = Button(text="Exit", width=10, command=qExit).grid(row=6, column=6)

window.mainloop()
