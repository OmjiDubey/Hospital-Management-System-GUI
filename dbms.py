import mysql.connector as sql

con = sql.connect(host="localhost",user="root",password="access",database="GUI")
cur = con.cursor()
cur.execute("create database if not exists GUI")
cur.execute("create table if not exists doctor(doc_id varchar(7),f_name varchar(10),l_name varchar(10),dob varchar(11),gender varchar(10),contact varchar(11),specs varchar(15),addr varchar(50))")
cur.execute("create table if not exists patient(pat_id varchar(7),f_name varchar(10),l_name varchar(10),dob varchar(11),gender varchar(10),contact varchar(11),problem varchar(15),addr varchar(50))")
cur.execute("create table if not exists employee(emp_id varchar(7),f_name varchar(10),l_name varchar(10),dob varchar(11),gender varchar(10),contact varchar(11),dept varchar(15),addr varchar(50))")
