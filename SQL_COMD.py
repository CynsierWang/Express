# -*- coding: utf-8 -*-
import MySQLdb as mdb
import random

today = 17100808

def RandomNum(n):
    s=""
    for i in range(n):
        r = random.randint(0,35)
        if r<10:
            s=s+str(r)
        else:
            s=s+chr(r+55)
    return s

def SelectDB(DB,type, value):
    con = None
    cmd = "SELECT * FROM %s WHERE %s='%s'" % (DB,type, value)
    print cmd
    try:
        con = mdb.connect('localhost', 'root', 'zxcvacaly', 'express')
        cur = con.cursor()
        cur.execute(cmd)
        results = cur.fetchall()
    finally:
        if con:
            con.close()
    return results

def CreatePSW():
    rst=[1]
    while(rst!=()):
        psw = RandomNum(9)
        rst = SelectDB("lockers","password",psw)
    return psw

def CreateON():
    rst=[1]
    while(rst!=()):
        order_number = RandomNum(13)
        rst = SelectDB("package","order_number",order_number)
    print order_number
    return order_number

def InsertPackage(info):#[customer,phone_number,size,date,order_number]
    con = None
    cmd = "INSERT INTO package (customer,phone_number,size," \
          "data,is_in_locker,order_number) VALUES ('%s','%s'," \
          "'%s',%d,%d,'%s')" % (info[0],info[1],info[2],info[3],0,info[4])
    print cmd
    try:
        con = mdb.connect('localhost', 'root', 'zxcvacaly', 'express')
        cur = con.cursor()
        cur.execute(cmd)
        con.commit()
    except:
        con.rollback()
    con.close()

def DropPackage(order_number):#[customer,phone_number,size,date,order_number]
    con = None
    cmd = "DELETE FROM package WHERE order_number='%s'" % order_number
    print cmd
    try:
        con = mdb.connect('localhost', 'root', 'zxcvacaly', 'express')
        cur = con.cursor()
        cur.execute(cmd)
        con.commit()
    except:
        con.rollback()
    con.close()

def CleanLocker(site):#[site,order_number,size,date,password]
    con = None
    cmd = "UPDATE lockers SET is_empty=1,order_number=NULL," \
          "data=NULL,password=NULL WHERE site='%s'" %  site
    print cmd
    try:
        con = mdb.connect('localhost', 'root', 'zxcvacaly', 'express')
        cur = con.cursor()
        cur.execute(cmd)
        con.commit()
    except:
        con.rollback()
    con.close()

def FeedLocker(site,order_number):
    '''
    向某坐标的柜子放入某快递单号的快递
    将某单号的快递的 is in locker 信息改成 1
    '''
    psw = CreatePSW()
    print psw
    con = None
    cmd = "UPDATE lockers SET is_empty=0,order_number='%s'," \
          "data=%d,password='%s' WHERE site='%s'" % \
          (order_number,today,psw,site)
    cmd2= "UPDATE package SET is_in_locker=1 WHERE order_number='%s'" % \
          (order_number)
    print cmd
    print cmd2
    try:
        con = mdb.connect('localhost', 'root', 'zxcvacaly', 'express')
        cur = con.cursor()
        cur.execute(cmd)
        cur.execute(cmd2)
        con.commit()
    except:
        con.rollback()
    con.close()

def PickUp(psw):
    '''
    根据口令打开一个柜子，初始化柜子的信息，从package里删除快递的信息
    依据柜子的大小，从当前同样大小包裹中选一个最早的
    如果存在这样的包裹，塞进柜子
    返回柜子的坐标
    '''
    rst = SelectDB("lockers","password",psw)
    if(rst==()):
        return ['Z']
    else:
        CleanLocker(rst[0][0])
        DropPackage(rst[0][2])
        print rst[0][3],"size"
        newpac = SelectPackage(rst[0][3])
        print newpac,"***********"
        if(newpac!=None):
            FeedLocker(rst[0][0],newpac)
        return rst[0][0]

def SelectPackage(size):
    '''
    从当前同样大小包裹中选一个最早的
    '''
    con = None
    cmd = "SELECT * FROM package WHERE size='%s' and is_in_locker=0 order by data asc" % (size)
    print cmd
    try:
        con = mdb.connect('localhost', 'root', 'zxcvacaly', 'express')
        cur = con.cursor()
        cur.execute(cmd)
        results = cur.fetchall()
    finally:
        if con:
            con.close()
    if(results!=()):
        print results[0][5],"name"
        return results[0][5]