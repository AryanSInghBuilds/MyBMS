from MyBMS import *
import mysql.connector
# create database using
#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="password"
#)

#mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

con = mysql.connector.connect(host="localhost",user="root",password="arya2000",database="mydatabase")
cur = con.cursor()


#create table using code below 
#cur.execute("create table user (uid varchar(225),username varchar(225) NOT NULL,address varchar(225) NOT NULL,gender varchar(225),mobile varchar(225) NOT NULL,password varchar(225) NOT NULL)")
#cur.execute("create table soldto (BID varchar(225),username varchar(225))")
#cur.execute("create table bookTable (BID varchar(225),bname varchar(225),price varchar(225))")
bms()
