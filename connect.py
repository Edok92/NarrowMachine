#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:22:40 2018

@author: selimchehimi
"""

import psycopg2

def connect():
    try:
        conn = psycopg2.connect("dbname='narrow_db' user='' host='localhost' password=''")
    except:
        print("unable to connect")
    return conn


#try:
 #   conn = psycopg2.connect("dbname='narrow_db' user='' host='localhost' password=''")
#except:
 #   print("unable to connect")
    
#cur = conn.cursor()

#try:
    #cur.execute("SELECT * from dico")
 #   cur.execute("INSERT INTO dico VALUES ('bonjour' , 0 , 0 , 1 , 0 , 0 , 1)")
  #  conn.commit()
    
    #results = cur.fetchall()
    
    #for r in results:
     #  print (r)

#except:
 #   print("I can't SELECT from dico")
    
