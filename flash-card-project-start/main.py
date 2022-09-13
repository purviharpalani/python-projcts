BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas as pd

data=pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card={}

def next_card():
    global current_card
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word,text=current_card["French"])

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


window.after(3000, func=flip_card)

canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR )
card_image=PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_image)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

right_image=PhotoImage(file="images/right.png")
known_button=Button(image=right_image,highlightthickness=0,command=next_card)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()