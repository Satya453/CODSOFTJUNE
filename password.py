#python program to create pasword generator
#Task 3 given by CODSOFT

from tkinter import*
import tkinter as tk
import random,string
import pyperclip

root =Tk()
root.geometry("400x500")
root.title("PASSWORD GENERATOR")
root.resizable(False,False)
root.configure(bg='skyblue')
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

heading = Label(root,text='PASSWORD GENERATOR', font='arial 20 bold',fg='#CD0000',bd=5,bg='#B0E0E6',anchor="center").pack(pady=10)
pass_label = Label(root,text='USER INPUT LENGTH', font='Helvetica 10',bg='violet',width=20,anchor="center").pack(pady=5)
pass_len =IntVar()
Spinbox(root ,from_=8, to_=32 ,textvariable=pass_len ,font=('sans-serif',14)).pack(pady=10)
pass_str = StringVar()

def Generator():
    password =''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()-4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        pass_str.set(password)

btn1 = Button(root,text= "GENERATE PASSWORD", command=Generator,font='bold 10',bg="violet",anchor="center").pack(pady=5)
Entry(root,width=22,textvariable=pass_str,font=('bold',12,'bold')).pack(pady=5)
pass_label1 =Label(root,text='DISPLAY',font='helvetica 10',bg='violet',width=20,height=2,anchor="center").pack(pady=7)
Entry = tk.Entry(root,textvariable=pass_str,justify='center',fg="#00008B",bg='yellow',font=("Helvetica",30,"bold"))
Entry.place(x=50,y=270,width=300,height=70)
 
def copy_password():
    pyperclip.copy(pass_str.get())
btn2= Button(root,text='COPY TO CLIPBOARD',command =copy_password,font='bold 10',bg='#ADADAD',width=20,anchor="center")
btn2.place(x=100,y=370)
    
root.mainloop()
