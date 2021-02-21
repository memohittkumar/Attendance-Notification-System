from tkinter import *
from tkinter.font import Font


def Login():
    loginwindow=Tk()
    loginwindow.config(bg='black')
    loginwindow.title('Login')
    loginwindow.geometry("650x550+350+200")
    loginwindow.resizable(False,False)
    heading = Label(loginwindow, text='JAIN UNIVERSITY', bg='black', fg='green',font=('Ink Free',30,'bold')).place(x=160, y=10)
    loginLabel=Label(loginwindow,text='Login',bg='Black',fg='white',font=('Ink Free',25,'bold')).place(x=310,y=80)
    username_login=Label(loginwindow,text='USERNAME',bg='black',fg='white',font=('Ink Free',20)).place(x=150,y=180)
    password_login = Label(loginwindow, text='PASSWORD', bg='black', fg='white', font=('Ink Free', 20)).place(x=150,
                                                                                                              y=260)
    username_login_entry=Entry(loginwindow,width=20,font=('Ink Free',15)).place(x=380,y=180)
    password_login_entry = Entry(loginwindow, width=20, font=('Ink Free',15)).place(x=380, y=260)

    submit_login=Button(loginwindow,width=10,text='LOGIN',font=('Ink Free',15)).place(x=300,y=380)

    loginwindow.mainloop()


root=Tk()
root.config(bg='black')
root.title('Login')
root.geometry("650x550+350+200")
root.resizable(False,False)
headingfont=Font(family='Ink Free', size=30, weight='bold')
loginfont=Font(family='Ink Free', size=20)
detailsfont=Font(family='Ink Free', size=20)
for_entry_size=('Ink Free',15)
heading=Label(root, text='JAIN UNIVERSITY', bg='black', fg='green',font=headingfont).place(x=160,y=10)






loginheading=Button(root, text='LOGIN',command=Login, bg='white', fg='black',font=for_entry_size).place(x=380,y=480)
Signupheading=Label(root, text='SIGN UP', bg='black', fg='white',font=for_entry_size).place(x=300,y=80)

firstname=Label(root,text='First Name',bg='black', fg='white', font=detailsfont).place(x=150,y=150)
lastname=Label(root,text='Last Name', bg='black', fg='white', font=detailsfont).place(x=150,y=200)
subject_code=Label(root,text='Subject Code', bg='black', fg='white', font=detailsfont).place(x=150,y=250)
email=Label(root,text='Email', bg='black', fg='white', font=detailsfont).place(x=150,y=300)
password=Label(root,text='Password', bg='black', fg='white', font=detailsfont).place(x=150,y=350)
retype_password=Label(root,text='Retype Password', bg='black', fg='white', font=detailsfont).place(x=130,y=400)


#..............Entry For Details.............

firstname_entry=Entry(root,width=20,font=for_entry_size).place(x=350,y=150)
lastname_entry=Entry(root,width=20,font=for_entry_size).place(x=350,y=200)
subcode_entry=Entry(root,width=20,font=for_entry_size).place(x=350,y=250)
email_entry=Entry(root,width=20,font=for_entry_size).place(x=350,y=300)
password_entry=Entry(root,width=20,font=for_entry_size).place(x=350,y=350)
retype_password_entry=Entry(root,width=20,font=for_entry_size).place(x=350,y=400)
submit=Button(root,width=10,text='SUBMIT',font=for_entry_size).place(x=230,y=480)










root.mainloop()
