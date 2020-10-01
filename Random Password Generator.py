import random
from tkinter import *
from tkinter import messagebox as msg
bg_color='light blue'
win=Tk()
win.title('Random Password Generator')
win.configure(background=bg_color)


def password_generator(len,pass_entry):
   if int(len)<=7:
        msg.showinfo('Info','Your password should be greater than 7 Characters')
   else:                 
    try:
        len=int(len)
    except Exception:
       msg.showerror('Error','Input should be in integer')
    else:
        ready_pass=''
        for i in range(len):
            ready_pass+=random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ1234567890@#$%&*')
        pass_entry.delete(0,END)
        pass_entry.insert(0,ready_pass)

len_label=Label(win,text='Enter the length of the password:',font=('MV Boli',15,'bold'),bg=bg_color)
len_label.place(x=10,y=10)

len_entry=Entry(win,bd=2,font=('',13),width=20,bg=bg_color)
len_entry.place(x=390,y=15)

summit_btn=Button(win,bg='orange',command=lambda: password_generator(len_entry.get(),pass_entry),text='Submit').place(x=420,y=55)

pass_lbl=Label(win,text='Ready password',font=('MV Boli',15,'bold'),bg=bg_color)
pass_lbl.place(x=10,y=100)

pass_entry=Entry(win,font=('',13),bd=2,bg=bg_color)
pass_entry.place(x=195,y=105)

win.geometry('600x200+400+200')
win.mainloop()
