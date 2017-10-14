# -*- coding: utf-8 -*-
from Tkinter import *
import SQL_COMD as mdb

def FetchFunction():
    def SendPwd():
        psw = str(E1.get())
        site= list(mdb.PickUp(psw))
        if(site[0]=='Z'):
            l1["text"]="口令错误"
            l1["fg"]="blue"
            return
        id = "".join(site[1:])
        id = int(id)
        x=id%9-1
        y=id/9
        if(site[0]=='A'):
            DrawPacS(x,y)
        elif(site[0]=='B'):
            DrawPacM(x,y)
        else:
            DrawPacL(x,y)

    def clickPac(event):
        x = (event.x-5)/50
        if(event.y<145):
            z=1
            y=(event.y-5)/35
            DrawBoxS(x,y)
        elif(event.y<345):
            z=2
            y=(event.y-145)/50
            DrawBoxM(x,y)
        else:
            z=3
            y = (event.y-345)/70
            DrawBoxL(x,y)
        print x,y,event.y
    Locker = Tk()
    Locker.title("取快递")
    l1=Label(Locker)
    l1.pack()
    w = Canvas(Locker, width=460, height=640)
    w.bind('<Button-1>',clickPac)
    w.pack()

    def DrawBoxS(x,y):
        w.create_rectangle(x*50+5,y*35+5,x*50+55,y*35+40,fill='white')
    def DrawBoxM(x,y):
        w.create_rectangle(x*50+5,y*50+145,x*50+55,y*50+195,fill='white')
    def DrawBoxL(x,y):
        w.create_rectangle(x*50+5,y*70+345,x*50+55,y*70+415,fill='white')

    def DrawPacS(x,y):
        w.create_rectangle(x*50+10,y*35+10,x*50+50,y*35+35,fill="brown")
    def DrawPacM(x,y):
        w.create_rectangle(x*50+10,y*50+150,x*50+50,y*50+190,fill="brown")
    def DrawPacL(x,y):
        w.create_rectangle(x*50+10,y*70+350,x*50+50,y*70+410,fill="brown")

    for i in range(4):
        for j in range(9):
            DrawBoxS(j,i)
            DrawBoxM(j,i)
            DrawBoxL(j,i)

    E1 = Entry(Locker)
    E1.insert(0, '取货口令')
    E1.pack()
    BtnCal = Button(Locker, text="_(:_」∠)_", command=SendPwd)
    BtnCal.pack()
    Locker.mainloop()

on1=mdb.CreateON()
on2=mdb.CreateON()
on3=mdb.CreateON()
mdb.InsertPackage(['cus1','18811176968','S',mdb.today,on1])
mdb.InsertPackage(['cus2','18811176968','M',mdb.today,on2])
mdb.InsertPackage(['cus3','18811176968','L',mdb.today,on3])
mdb.FeedLocker('A1',on1)
mdb.FeedLocker('B1',on2)
mdb.FeedLocker('C1',on3)

FetchFunction()