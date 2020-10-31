from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="arya2000"
)

mycursor = mydb.cursor()



mypass = "arya2000"
mydatabase="mydatabase"


con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
 
bookTable = "bookTable" #Book Table
user="user"#user table

def buyBook():
    
    bid = bookInfo1.get()
    uid = userInfo1.get()
    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    msg = "select address from user where uid ='"+uid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(msg)
        for x in cur:
            msg1=x
        con.commit()
        
        messagebox.showinfo('Success',"Book will be delivered to "+msg1[0]+" address")
        file = open('records.txt','a') 
        file.write("\n user ID "+uid+" bought book with book ID = "+bid) 
        file.close()
    except:
        messagebox.showinfo("Please check Book ID")
    

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()
    
def buy(): 
    
    global bookInfo1,userInfo1,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Buy Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to buy
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    lb2 = Label(labelFrame,text="UID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3)
        
    userInfo1 = Entry(labelFrame)
    userInfo1.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=buyBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()