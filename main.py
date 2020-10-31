from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox

from buybook import *
from ViewBooks import *

from ReturnBook import *
from sellbook import *

# Add your own database name and password here to reflect in the code
mypass = "arya2000"
mydatabase="mydatabase"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()


def main():
    
    global rooot
    rooot = Tk()
    rooot.title("main")
    rooot.minsize(width=400,height=400)
    rooot.geometry("600x500")

    
   

    # Adding a background image img = tkinter.PhotoImage(file="lib.png")

    Canvas1 = Canvas(rooot)

          
    Canvas1.config(bg="#395697",width = 600, height = 500)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(rooot,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="My Book Management\n system", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(rooot,text="SELL BOOKS",bg='black', fg='white', command=sellbook)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(rooot,text="BUY BOOKS",bg='black', fg='white', command=buy)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(rooot,text="AVAILABLE BOOKS",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(rooot,text="QUIT",bg='black', fg='white', command = rooot.destroy)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    rooot.mainloop()
