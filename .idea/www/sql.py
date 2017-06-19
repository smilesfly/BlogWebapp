#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(host='localhost', port=3306,user='root',passwd='root',db='awesome',charset='UTF8') #连接MySQL数据库中的awesome数据库
cursor = conn.cursor()#创建游标
cursor.execute('create table users (id varchar(50) primary key,email varchar(50),passwd varchar(50),name varchar(50),image varchar(500),admin boolean,create_at real)')#创建users表-->表列都要定义名字及类型，主键后还要跟primary key
cursor.execute('create table blogs (id varchar(50) primary key,user_id varchar(50),user_name varchar(50),user_image varchar(500),name varchar(50),summary varchar(200),content text,create_at real)')#创建blogs表
cursor.execute('create table comments (id varchar(50) primary key,blog_id varchar(50),user_id varchar(50),user_name varchar(50),user_image varchar(500),content text,create_at real)')#创建comments表
cursor.close()
conn.commit()
conn.close()