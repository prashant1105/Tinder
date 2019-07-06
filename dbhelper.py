#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:09:30 2019

@author: prashantpk
"""

import mysql.connector

class DBHelper:
    
##------------------------------- CONSTRUCTOR for Class DBHelper -----------------------##
    
    def __init__(self):
        try:
            self._connection = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "",    database = "tinderb3")
            self._cursor = self._connection.cursor()
            print("Connected to Database.")
            
        except:
            print("Could not connect to Database.")
            #exit(0)
            
##------------------------------------- Function End -------------------------------------##


##------------------------ Function for Searching in the Database ------------------------##
# This function will search in the database with two keys and their respective values.
            
    def search(self, key1, value1, key2, value2, table):
        self._cursor.execute("""
        SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'
        """.format(table, key1, value1, key2, value2))
        data = self._cursor.fetchall()
        return data
    
##------------------------------------- Function End -------------------------------------##
        

##------------------------ Function for Searching in the Database ------------------------##
# This function will search in the database with only one keys and their respective values.
    
    def searchOne(self, key1, value1, table, type1):
        
        #query = 
        self._cursor.execute("""
        SELECT * FROM `{}` WHERE `{}` {} '{}' """.format(table, key1, type1, value1))
        data = self._cursor.fetchall()
        return data
    
##------------------------------------- Function End -------------------------------------##


##--------------------- Function for Searching Values in the Database --------------------##         
    
    def searchOneFromList(self,key1,value1,table,type):
        #print("""
            #select * from `{}` WHERE `{}` {} {}
            #""".format(table,key1,type,value1))
        self._cursor.execute("""
            select * from `{}` WHERE `{}` {} {}
            """.format(table,key1,type,value1))
        
        data=self._cursor.fetchall()
        
        return data
    
##------------------------------------- Function End -------------------------------------##
        
    
##--------------------- Function for Inserting Values in the Database --------------------##    
# A general function for inserting values in a table... Can be used for any table with any number of columns...    
    
    def insert(self, insertDict, table):    
        colValue = ""
        dataValue = ""
        for i in insertDict:
            colValue = colValue + "`" + i + "`,"
            dataValue = dataValue + "'" + insertDict[i] + "',"
        colValue = colValue[0 : -1]
        dataValue = dataValue[0 : -1]
        
        query = "INSERT INTO `{}` ({}) VALUES ({})".format(table, colValue, dataValue)
        #print(query)
        try:
            self._cursor.execute(query)
            self._connection.commit()
            return 1
        except:
            return 0
        
##------------------------------------- Function End -------------------------------------##
            
        
##---------------------- Function for Updating Data in the Database ----------------------##
            
    def update(self, insertDict, table, sessionId):
        query = """
        UPDATE `{}` SET `name` = '{}', `password` = '{}', `gender` = '{}', `age` = '{}', `city` = '{}', `dp` = '{}' WHERE user_id = {}""".format(table, insertDict['name'], insertDict['password'], insertDict['gender'], insertDict['age'], insertDict['city'], insertDict['dp'], sessionId)
        #print(query)
        try:
            self._cursor.execute(query)
            self._connection.commit()
            return 1
        
        except:
            return 0        
        
##------------------------------------- Function End -------------------------------------##