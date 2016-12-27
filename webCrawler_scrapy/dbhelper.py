#!/usr/bin/python
#coding=utf-8
import MySQLdb
from scrapy.utils.project import get_project_settings

class DBHelper():
    
    def __init__(self):
        self.settings=get_project_settings()
        
        self.host=self.settings['MYSQL_HOST']
        self.port=self.settings['MYSQL_PORT']
        self.user=self.settings['MYSQL_USER']
        self.passwd=self.settings['MYSQL_PASSWD']
        self.db=self.settings['MYSQL_DBNAME']
    
    def connectMysql(self):
        conn=MySQLdb.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             charset='utf8')
        return conn
    def connectDatabase(self):
        conn=MySQLdb.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.db,
                             charset='utf8')
        return conn   
    
    def createDatabase(self):
        conn=self.connectMysql()
        sql="create database if not exists "+self.db
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
    
    def createTable(self,sql):
        conn=self.connectDatabase()
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    def insert(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor();
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()

    def update(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()#×¢ÒâÒªcommit
        cur.close()
        conn.close()
    
    def delete(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
        
        
class TestDBHelper():
    def __init__(self):
        self.dbHelper=DBHelper()
               
    def testCreateDatebase(self):
        self.dbHelper.createDatabase() 

    def testCreateTable(self):
        sql="create table testtable(id int primary key auto_increment,name varchar(50),url varchar(200))"
        self.dbHelper.createTable(sql)

    def testInsert(self):
        sql="insert into testtable(name,url) values(%s,%s)"
        params=("test","test")
        self.dbHelper.insert(sql,*params)

    def testUpdate(self):
        sql="update testtable set name=%s,url=%s where id=%s"
        params=("update","update","1")
        self.dbHelper.update(sql,*params)
    
    def testDelete(self):
        sql="delete from testtable where id=%s"
        params=("1")
        self.dbHelper.delete(sql,*params)
    
if __name__=="__main__":
    testDBHelper=TestDBHelper()
    testDBHelper.testCreateDatebase()
    testDBHelper.testCreateTable()