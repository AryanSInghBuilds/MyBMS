from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from main import *
from ViewBooks import *
user="user"        


##############################################################################################################################################


def userRegister():
    
    uid = userInfo1.get()
    name = userInfo2.get()
    add = userInfo3.get()
    gender = userInfo4.get()
    mobile = userInfo5.get()
    password = userInfo6.get()
    
    insertUser = "insert into "+user+" values('"+uid+"','"+name+"','"+add+"','"+gender+"','"+mobile+"','"+password+"')"
    try:
        cur.execute(insertUser)
        con.commit()
        messagebox.showinfo('Success',"User registered successfully")
        file = open('records.txt','a') 
        file.write("\n "+name+" , user ID "+uid+" Registered in ") 
        file.close()
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    

    print(uid)
    print(name)
    print(add)
    print(gender)
    print(mobile)
    print(password)
    
    
    root.destroy()


#################################################################################################################################################



def register(): 
    
    global userInfo1,userInfo2,userInfo3,userInfo4,userInfo5,userInfo6,Canvas1,con,cur,user,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    # Add your own database name and password here to reflect in the code
    mypass = "arya2000"
    mydatabase="mydatabase"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    user = "user" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="User Registeration", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # User ID
    lb1 = Label(labelFrame,text="User ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1, relheight=0.08)
        
    userInfo1 = Entry(labelFrame)
    userInfo1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08)
        
    # user name
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
        
    userInfo2 = Entry(labelFrame)
    userInfo2.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
        
    # Address of user
    lb3 = Label(labelFrame,text="Address : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.40, relheight=0.08)
        
    userInfo3 = Entry(labelFrame)
    userInfo3.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.08)
        
    # User Gender
    lb4 = Label(labelFrame,text="Gender(male/female) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.55, relheight=0.08)
        
    userInfo4 = Entry(labelFrame)
    userInfo4.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)

    # User mobile number
    lb5 = Label(labelFrame,text="Phone no. : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.70, relheight=0.08)
        
    userInfo5 = Entry(labelFrame)
    userInfo5.place(relx=0.3,rely=0.70, relwidth=0.62, relheight=0.08)

    # User password
    lb6 = Label(labelFrame,text=" Password : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.85, relheight=0.08)
        
    userInfo6 = Entry(labelFrame)
    userInfo6.place(relx=0.3,rely=0.85, relwidth=0.62, relheight=0.08)

   
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=userRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


#######################################################################################################################################3


def loginuser():
      #name of table containing users
    global SubmitBtn,labelFrame,u1,u6,lb1,Canvas1,con,cur,user,root
    uid=u1.get()
    password=u6.get()
    root.destroy()
    coin=0
    loginSql = "select uid from user where password='"+password+"' and uid='"+uid+"'"
    
    try:
        cur.execute(loginSql)
        
        for x in cur:
            mun=x
        con.commit()
        if(mun[0]==uid):
            messagebox.showinfo('Success',"logged in Successfully")
            coin=coin+1
            file = open('records.txt','a') 
            file.write("\n user ID "+uid+" logged in ") 
            file.close()
            print(uid)
            print(password)
            
    except:
        messagebox.showinfo('Error',"Please check User ID or Password")

    if(coin!=0):
        main()
    
#########################################################################################################################################



def login():
    
    global SubmitBtn,labelFrame,u1,u6,lb1,Canvas1,con,cur,user,root
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500") 

    mypass = "arya2000"
    mydatabase="mydatabase"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()  
    
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="login portal", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    # User ID
    lb1 = Label(labelFrame,text="User ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    u1 = Entry(labelFrame)
    u1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    
    lb2 = Label(labelFrame,text="password : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4, relheight=0.08)
        
    u6 = Entry(labelFrame)
    u6.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=loginuser)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    

##########################################################################################################################################



def bms():
    global root1
    root1=Tk()
    root1.title("My BMS")
    root1.minsize(width=400,height=400)
    root1.geometry("600x500")

    # Take n greater than 0.25 and less than 5
    same=True
    n=0.25

    # Adding a background image
    background_image =Image.open("lib.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
    
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root1)

    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root1,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="welcome to MyBMS", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root1,text="Login your account",bg='black', fg='white', command=login)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root1,text="new User Register",bg='black', fg='white', command=register)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    btn3 = Button(root1,text="Books Available",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn4 = Button(root1,text="EXIT",bg='black', fg='white', command=root1.destroy)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    root1.mainloop()   



    




