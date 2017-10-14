# -*- coding: utf-8 -*-
from Tkinter import *
import SQL_COMD as mdb

def FeedFunction():
    def SendPac():
        global v
        info=[]
        info.append(str(E1.get()))
        info.append(str(E2.get()))
        info.append(str(E7.get()))
        info.append(mdb.today)
        info.append(mdb.CreateON())
        print info
    Locker = Tk()
    Locker.title("快递员揽货")
    E1 = Entry(Locker)
    E1.insert(0, '收件姓名')
    E2 = Entry(Locker)
    E2.insert(0, '收件人联系电话')
    E3 = Entry(Locker)
    E3.insert(0, '收件人地址')
    E4 = Entry(Locker)
    E4.insert(0, '寄件人姓名')
    E5 = Entry(Locker)
    E5.insert(0, '寄件人联系电话')
    E6 = Entry(Locker)
    E6.insert(0, '寄件人地址')
    E7 = Entry(Locker)
    E7.insert(0, 'S/M/L')
    E1.pack()
    E2.pack()
    E3.pack()
    E4.pack()
    E5.pack()
    E6.pack()
    E7.pack()
    BtnCal = Button(Locker, text="_(:_」∠)_", command=SendPac)
    BtnCal.pack()
    Locker.mainloop()

