## Building login and registration page
## Automated webbrower

import mysql.connector
from tkinter import*
import webbrowser

class Browser:
    def __init__(self):
        self.root=Tk()

        self.root.title("shruti search engine")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)
        self.root.configure(background="#2ecc71")

        label1=Label(self.root,text="Search Engine",bg="#2ecc71",fg="#ffffff")
        label1.configure(font=("Constantia",22,"bold"))
        label1.pack(pady=(30,10)) #geometry 

        self.url=Entry(self.root)
        self.url.pack(ipadx=40,ipady=5)

        click=Button(self.root,text="Fetch",bg="#ffffff",width=28,height=2,command=lambda:self.fetch())
        click.pack(pady=(10,20))

        #self.result=Label(self.root,bg="#2ecc71",fg="#ffffff")
        #self.result.configure(font=("Constantia",14))
        #self.result.pack(pady=(5,10))

        self.root.mainloop()
        
    def fetch(self):
        url=self.url.get()
        print(url)
        webbrowser.open(url)
class Swiggy:
    def __init__(self):
        self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="hit")
        self.mycursor=self.conn.cursor()
        self.root=Tk()
        self.root.title(" :) Swiggy HomePage :)")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)
        self.root.configure(background="#0000ff")

        label1=Label(self.root,text="Registration page",bg="#0000ff",fg="#ffffff")
        label1.configure(font=("Constantia",22,"bold"))
        #label1.pack(pady=(30,10))
        label1.grid(row=0, column=1)
        
        #a = Label(self.root ,text = "Name").grid(row = 0,column = 0)
        #b = Label(self.root ,text = "Email").grid(row = 1,column = 0)
        #c = Label(self.root ,text = "Password").grid(row = 2,column =0)

        # create name label
        # create grid for position
        name = Label(self.root, text="Name", bg="#0000ff" ,fg="#ffffff")
        name.configure(font=("Constantia",15,"bold"))
        name.grid(row=1, column=0, sticky=W)
        #name.pack(padx=0, pady=0, side=LEFT)

        # create email label
        email = Label(self.root, text="Email Id", bg="#0000ff" ,fg="#ffffff")
        email.configure(font=("Constantia",15,"bold"))
        email.grid(row=2, column=0, sticky=W)
        #email.pack(padx=5, pady=0, )
        
        # create password label
        password = Label(self.root, text="Password", bg="#0000ff" ,fg="#ffffff")
        password.configure(font=("Constantia",15,"bold"))
        password.grid(row=3, column=0, sticky=W)
        #password.pack(padx=5, pady=0, )

        #create a text entry box for name,email,password label
        self.name_field = Entry(self.root)
        self.name_field.grid(row=1, column=1, ipadx=40, ipady=5)

        self.email_field = Entry(self.root)
        self.email_field.grid(row=2, column=1, ipadx=40, ipady=5)

        self.password_field = Entry(self.root)
        self.password_field.grid(row=3, column=1, ipadx=40, ipady=5)

        # create submit button 
        click=Button(self.root,text="submit",bg="#ff1a1a",width=28,height=2,command=lambda:self.Register())
        click.grid(row=8, column=1)

        self.result=Label(self.root,bg="#FFFF00",fg="#800080")
        self.result.configure(font=("Constantia",14))
        self.result.grid(row=25,column=1)
        
  
        self.root.mainloop()

    def Register(self):
        name=self.name_field.get() #get(): give the entry value
        print(name)
        email=self.email_field.get()
        print(email)
        password=self.password_field.get()
        print(password)
        self.mycursor.execute("INSERT INTO users (user_id,name,email,password) VALUES (NULL,'{}','{}','{}')".format(name,email,password))
        self.conn.commit()
        show="Register successfully"
        self.result.configure(text=show)

class Swiggy1(Swiggy,Browser):
    def __init__(self):
        self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="hit")
        self.mycursor=self.conn.cursor()
        self.root=Tk()
        self.root.title(" :) Login home page :)")
        self.root.minsize(400,600)
        #self.root.maxsize(400,600)
        self.root.configure(background="#0000ff")

        label1=Label(self.root,text="login page",bg="#0000ff",fg="#ffffff")
        label1.configure(font=("Constantia",22,"bold"))
        #label1.pack(pady=(30,10))
        label1.grid(row=0, column=1)
        
        #a = Label(self.root ,text = "Name").grid(row = 0,column = 0)
        #b = Label(self.root ,text = "Email").grid(row = 1,column = 0)
        #c = Label(self.root ,text = "Password").grid(row = 2,column =0)

        # create name label
        # create grid for position
        
        #name.pack(padx=0, pady=0, side=LEFT)

        # create email label
        email = Label(self.root, text="Email Id", bg="#0000ff" ,fg="#ffffff")
        email.configure(font=("Constantia",15,"bold"))
        email.grid(row=2, column=0, sticky=W)
        #email.pack(padx=5, pady=0, )
        
        # create password label
        password = Label(self.root, text="Password", bg="#0000ff" ,fg="#ffffff")
        password.configure(font=("Constantia",15,"bold"))
        password.grid(row=3, column=0, sticky=W)
        #password.pack(padx=5, pady=0, )

        #create a text entry box for name,email,password label
        

        self.email_field = Entry(self.root)
        self.email_field.grid(row=2, column=1, ipadx=40, ipady=5)

        self.password_field = Entry(self.root)
        self.password_field.grid(row=3, column=1, ipadx=40, ipady=5)

        # create submit button 
        click=Button(self.root,text="submit",bg="#ff1a1a",width=28,height=2,command=lambda:self.login())
        click.grid(row=8, column=1)

        click1=Button(self.root,text="Register",bg="#ff1a1a",width=28,height=2,command=lambda:super(Swiggy1,self).__init__())
        click1.grid(row=10, column=1)

        click2=Button(self.root,text="search",bg="#ff1a1a",width=28,height=2,command=lambda:Browser().__init__())
        click2.grid(row=12, column=1)

        ## To print the stuffs on login page
        self.result=Label(self.root,bg="#2ecc71",fg="#ffffff")
        self.result.configure(font=("Constantia",14))
        self.result.grid(row=25,column=1)
        
        
        self.root.mainloop()


    def login(self):
        email=self.email_field.get()
        print(email)
        password=self.password_field.get()
        print(password)
        self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}'AND password LIKE '{}'".format(email,password))
        if len(self.mycursor.fetchall())==0:
            show="Incorrect credentials!! please try once again"
            self.result.configure(text=show)
            
           # super.Register(self)
        else:
            show="WELCOME BACK !!"
            self.result.configure(text=show)
            
            

obj1=Swiggy1()









        
