import sys
import logging
from src import rds_config
import pymysql
import os
import requests
import json
import time


rds_host = rds_config.db_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
port = 3306
logger = logging.getLogger()
logger.setLevel(logging.INFO)
APIKEY = "58c66e96f312aedb78f7f726e5da74ec7ade7e33"
NAME = "Dublin"
STATIONS_URL = "https://api.jcdecaux.com/vls/v1/stations"
try:
    conn = pymysql.connect(rds_host, user=name,
    passwd=password, db=db_name, connect_timeout=10000)
    
    print('yup')
    test = True
    
    
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    test = False
    sys.exit()

def parse():
    if test == True:
#         conn = pymysql.connect(rds_host, user=name,
#         passwd=password, db=db_name, connect_timeout=10000)
        curs = conn.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS DublinBikestest101(
        number INT(4) NOT NULL,
        name VARCHAR(45) NOT NULL,
        status VARCHAR(10) NOT NULL,
        bike_stands INT(4) NOT NULL,
        available_bike_stands INT(4) NOT NULL,
        available_bikes INT(4) NOT NULL,        
        last_update BIGINT(15) NOT NULL
        )ENGINE=InnoDB'''
        curs.execute(sql)
        r = requests.get(STATIONS_URL, params={"apiKey": APIKEY, "contract": NAME})
        result = json.loads(r.text)
        
        for i in range(101):
            rowlist = []
            line = result[i]
            for a,b in line.items():
                temp = b
                if a == "position" or a== "address" or a =="contract_name" or a == "bonus" or a == "banking": 
                    pass
                else:
                    rowlist.append(temp)
                    rowlist1 = tuple(rowlist)
            print (rowlist1)
                 

            INPUT = "INSERT INTO DublinBikestest101 VALUES {0}".format(rowlist1)
            #print (INPUT)
            curs.execute(INPUT)
        conn.commit()
        curs.close()
        
            #print (line.values())      
        
            
parse()