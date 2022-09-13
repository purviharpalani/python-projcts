from tkinter import *

window=Tk()
window.title("Mile to Km Convertor")
# window.minsize()
window.config(padx=30,pady=30)

# entry
input=Entry(width=10)
input.grid(column=1,row=0)

#label
l1=Label(text="Miles")
l1.grid(column=2,row=0)

l2=Label(text="is equal to")
l2.grid(column=0,row=1)

l3=Label(text="0")
l3.grid(column=1,row=1)

l4=Label(text="Km")
l4.grid(row=1,column=2)

def button_Clicked():
    miles=input.get()
    miles=float(miles)
    km=miles * 1.609
    l3["text"]=km
    l3.grid(column=1,row=1)


# button
button=Button(text="Calculate",command=button_Clicked)
button.grid(row=2,column=1)

window.mainloop()