#python program to create simple calculator
#Task 2 given by codsoft

import tkinter as tk

def on_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0,tk.END)
            entry.insert(tk.END,str(result))
        except Exception as e:
            entry.delete(0,tk.END)
            entry.insert(tk.END, "Error")
    elif text == "AC":
        entry.delete(0,tk.END)
    elif text =="del":
        lenght = len(current_text)-1
        entry.delete(lenght)
    else:
        entry.insert(tk.END,text)

def create_button(text, row, col, col_span=1):
    button = tk.Button(root,text=text,font=("Helvetica",18),bd=5)
    button.grid(row=row,column=col,columnspan=col_span,padx=5,pady=5)
    button.bind("<Button-1>",on_click)
    return button

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
heading_label = tk.Label(root,text="Calculator", font=("Helvetica",16,"bold"),highlightcolor=("green"))
heading_label.grid(row=0,column=0,columnspan=4,pady=20)
entry = tk.Entry(root,font=("Helvetica",24),bd=5,justify=tk.RIGHT)
entry.grid(row=1,column=0,columnspan=4,padx=10,pady=10)

create_button("AC",2,0)
create_button("()",2,1)
create_button("%",2,2)
create_button("/",2,3)

create_button("7",3,0)
create_button("8",3,1)
create_button("9",3,2)
create_button("*",3,3)

create_button("4",4,0)
create_button("5",4,1)
create_button("6",4,2)
create_button("-",4,3)

create_button("1",5,0)
create_button("2",5,1)
create_button("3",5,2)
create_button("+",5,3)

create_button("0",6,0)
create_button(".",6,1)
create_button("del",6,2)
create_button("=",6,3)

root.mainloop()