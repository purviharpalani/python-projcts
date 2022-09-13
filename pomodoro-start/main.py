from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label["text"]="Timer"
    canvas.itemconfig(timer_text, text="00.00")
    checkmark_label.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec=LONG_BREAK_MIN*60

    # if it's the 8th rep
    if reps %8==0:
        countdown(long_break_sec)
        timer_label["text"]="Break"
        timer_label["fg"]=RED

    # if it's 2nd/4th/6th rep
    elif reps%2==0:
        countdown(short_break_sec)
        timer_label["text"] = "Break"
        timer_label["fg"] = PINK
        # timer_label.config(text="Break",fg=PINK)

    # if it's the 1st/3rd/5th/7th rep:
    else:
        countdown(work_sec)
        timer_label["text"] = "Work"
        timer_label["fg"] = GREEN



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min<10:
        count_min=f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer=window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
        checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



timer_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
timer_label.grid(row=0,column=1)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00.00",fill="white",font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1,column=1)


#  start button
button1=Button(text="Start", highlightthickness=0, command=start_timer)
button1.grid(row=2,column=0)

button2=Button(text="Reset",highlightthickness=0,command=reset_timer)
button2.grid(row=2,column=2)

checkmark_label=Label(fg=GREEN,bg=YELLOW)
checkmark_label.grid(row=3,column=1)



window.mainloop()