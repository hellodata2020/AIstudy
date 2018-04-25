import MySQLdb
from artlog import *
import random

class initmysql():
    def __init__(self,username,passwd,ipaddr,dbname,dbport,dbcharset):
        try:
            self.db=MySQLdb.connect(ipaddr,username,passwd,dbname,port=dbport)
        except Exception,e:
            print e.message
            errlog("messages.log",e.message)


    def readtablesql(self, sql):
        try:
            self.res = []
            initcursor = self.db.cursor()
            initcursor.execute(sql)
            self.db.commit()
            reports = initcursor.fetchall()
            listreports = list(reports)
            for idreports in listreports:
                self.res.append(idreports[0])

            print self.res

        except Exception, e:
            errlog("messages.log", e.message)
            print e.message
            self.db.rollback()

    def writetablesql(self,sql):
        try:
            self.res = []
            initcursor = self.db.cursor()
            initcursor.execute(sql)
            self.db.commit()
            return True

        except Exception,e:
            errlog("messages.log", e.message)
            print e.message
            self.db.rollback()
            return False




    def closedb(self):
        self.db.close()




def main():
    litedb = initmysql('bodie','sonyw320','127.0.0.1','db',3306,'utf-8')
    litedb.readtablesql("show databases;")
    litedb.closedb()

def creatbigtable():
    bigdb = initmysql('bodie','sonyw320','127.0.0.1','db',3306,'utf-8')

    # create table
    # create table wxid(id int(10) not null,name varchar(32) not null,qqnumber int(12) not null,sex bit default 0,city varchar(30) default 'hangzhou',index firstindex (qqnumber ASC),primary key (id));



    for time in range(1,100000):
        try:
            randomid = int(''.join(str(random.choice(range(10))) for _ in range(10)) )
            randomnum = int(''.join(str(random.choice(range(10))) for _ in range(10)) )
            comsql = "insert into wxid (id,name,qqnumber,sex,city) values (%d,'lesux',%d,sex,city);" % (randomid,randomnum)
            bigdb.writetablesql(comsql)
        except Exception,e:
            pass
    bigdb.closedb()








if __name__ == '__main__':
    # main()
    creatbigtable()
