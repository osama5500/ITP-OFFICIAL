from tkinter import *
from PIL import Image, ImageTk

window = Tk()

window.geometry("800x800")

window.title("Injoy")

injoyCover = ImageTk.PhotoImage(Image.open('injoyable.jpeg').resize((150, 150)))

window.iconphoto(True,injoyCover)

window.config(bg="#fae5b1")

goxanLabel = Label(window, 
pady=5,
text="aint got no bag i just aluminium foil it",
bg="#fae5b1", fg ="black",
font=('Arial', 20,'bold'),
relief=RAISED,
padx=5,
image=injoyCover)

goxanLabel.pack()

count = 0

def click():
    global count
    count+=1
    print("wigan out " + str(count))

def submit():
    username = dearDiary.get()
    print("wsg goxan twin " + str(username))
    dearDiary.config(state=DISABLED)

def delete():
    dearDiary.delete(0,END)

def backspace():
    dearDiary.delete(len(dearDiary.get()) -1, END)

wiganButton = Button(window,
                     text = "goxan button!!",  
                    command = click,
                    bg="#fae5b1",
                    fg='black',
                    relief=RAISED,
                    bd=5,
                    activebackground="#fae5b1",
                    activeforeground='black') #compound='top'

wiganButton.pack()

dearDiary = Entry(window,
                 text="submit",
                 fg="#fae5b1",
                 bg='black',
                 )
dearDiary.insert(0,'LAZER DIM 700')

dearDiary.pack(side=LEFT)

submit_button = Button(window,text="goxan here!", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="no, goxan slime", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="remove a SINGLE goxan here!", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()