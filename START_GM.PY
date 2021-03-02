import tkinter as tk
import random

window = tk.Tk()
window.geometry("340x350")
window.minsize(340,350)
window.maxsize(340,350)
window.title("ROCK PAPER SCISSORS GAME")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def choice_to_number(choice):
    rps={'rock':0,'paper':2,'scissor':3}
    return rps[choice]

def number_to_choice(number):
    rps={0:'rock',1:'paper',3:'scissor'}
    return rps[number]

def random_comp_choice():
    return random.choice(['rock','paper','scissor'])

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE

    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if (user==comp):
        print("ITS A TIE")
    elif((user-comp)%3==1):
        print("YOU WIN")
        USER_SCORE+=1
    else:
        print("COMP WIN")
        COMP_SCORE+=1
    
    text_area= tk.Text(font="elegant 11 bold",height=12,width=40,bg='gray',borderwidth=3,fg="green")
    text_area.grid(columnspan=3,row=2)
    answer= f"your choice:  {USER_CHOICE} \nComputer's choice: {COMP_CHOICE}\nYour Score: {USER_SCORE}\nComputer Score: {COMP_SCORE}"
    text_area.insert(tk.END,answer)

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_comp_choice()
    result(USER_CHOICE,COMP_CHOICE)

def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_comp_choice()
    result(USER_CHOICE,COMP_CHOICE)

def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_comp_choice()
    result(USER_CHOICE,COMP_CHOICE)

button1= tk.Button(text="Rock",font="elegant 12 bold",bg="skyblue",width=8,height=5,command=rock,borderwidth=3)
button1.grid(column=0,row=1,pady=5,padx=10)

button2= tk.Button(text="Paper", font="elegant 12 bold",bg="skyblue",width=8,height=5,command=paper, borderwidth=3)
button2.grid(column=1,row=1,pady=5,padx=10)

button3= tk.Button(text="Scissor",font="elegant 12 bold",bg="skyblue",width=8,height=5,command=scissor,borderwidth=3)
button3.grid(column=2,row=1,pady=5,padx=10)

window.mainloop()