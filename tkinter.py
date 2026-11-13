from tkinter import*
from tkinker import messagebox
root=Tk() #box will display
root.geometry('700x700') #WxH
root.title("college Management")
root.maxsize(width=800,height=800)
root.minsize(width=200,height=200)
root.configure(bg='blue')  #for standard VIBGYOR
root.configure(bg='#00FFFF') #colour code

#place, pack, grid
a=Label(root,text="Welcome", font=('times','30','bold'),fg='red',bg='#00FFFF')
##a.place(x=100,y=200)
a.pack()
##a.grid(row=0,column=0)

name=StringVar()
##name=IntVar()

en=Entry(root,width=10,textvariable=name)
en.pack()
#print(name.get())
def but():
    print(en.get())
    
##but()
a.pack()
en=Entry(root,width=0,justify='center')
en.pack()
b=Button(root,text='submit',command=but)
b.pack()

root.mainloop()#Like end line,run without it also.
#Label,Button-->relief='solid'
#relief=solid,sunken,ridge,groove,raised,flat.

def n():
    r=Tk() #separate page
    r=Toplevel() #continue page

b=Button(root,text='next page',command=n)
b.pack()


def close():
    root.destroy()
    print("okay")

messagebox.showinfo('your title','okay')
#messagebox,showinfo, showwarning, showerror, askquestion, askyesno, askretrycancel.



