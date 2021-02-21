from tkinter import *
import datetime

date = datetime.datetime.now().date()
date = str(date)

class Application(object):
    def __init__(self, master):
        self.master = master

        #..........Frames.................

        self.top=Frame(master, height=150, bg='Black')
        self.top.pack(fill=X)

        self.bottom=Frame(master, height=500,bg='#219dcd')
        self.bottom.pack(fill=X)


        #.....Top Frame Components.............
        self.icon = PhotoImage(file='icons/a.png')
        self.icon_label=Label(self.top,image=self.icon)
        self.icon_label.place(x=10,y=10)

        self.heading=Label(self.top, text="Faculty Profile", font='Aerial 40 bold',bg='black',fg='#ebb434')
        self.heading.place(x=180,y=20)

        self.date_lable=Label(self.top,text="Today's Date "+date,bg='black',font='aerial 15 bold', fg='#ebb434')
        self.date_lable.place(x=250,y=100)



        #...........BOTTOM Frame Components..............

        self.namelabel=Label(self.bottom, text='Faculty Name', font='Aerial 20 bold',bg='#219dcd', fg='black')
        self.namelabel.place(x=0,y=10)

        self.usnlabel = Label(self.bottom, text='Subject Code', font='Aerial 20 bold', bg='#219dcd', fg='black')
        self.usnlabel.place(x=0, y=80)

        self.emaillabel = Label(self.bottom, text='Email', font='Aerial 20 bold', bg='#219dcd', fg='black')
        self.emaillabel.place(x=0, y=150)

        self.Enter_attendance = Button(self.bottom, text='Enter Attendance',width=15, font='Aerial 20 bold', bg='black', fg='#ebb434')
        self.Enter_attendance.place(x=50,y=240)

        self.Enter_marks = Button(self.bottom, text='Enter Marks',width=15, font='Aerial 20 bold', bg='black',fg='#ebb434')
        self.Enter_marks.place(x=330, y=240)
















def main():
    root=Tk()
    app=Application(root)
    root.title("Profile")
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()



if __name__=='__main__':
    main()
