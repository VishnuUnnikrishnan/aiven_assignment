#The Database class writes to the database.
import psycopg2 as pg
from . import log
from datetime import datetime

class dbwriter:

    #initialise class
    def __init__(self, host="localhost", port=5432, dbname="pageup", user="postgres", password=None, table="pageup", protocol=None):
        self.table = table
        uri = ""
        port = str(port)

        try:
            if protocol == None:
                uri = "postgres://"+user+":"+password+"@"+host+":"+port+"/"+dbname
            
            elif protocol == "SSL":
                uri = "postgres://"+user+":"+password+"@"+host+":"+port+"/"+dbname+"?sslmode=require"
            else:
                log.log_error("Unable to create URI","Protocol not supported")
            
            conn = pg.connect(uri)
            cursor = conn.cursor()
            self.conn = conn
            self.cursor = cursor

        except Exception as e:
            log.log_error("Unable to create connection", e)

    #Write to DB 
    def write(self, msg):
        
        # SQL injection is not a concern here because there is no user input, 
        # and if they can edit variables, then they have access to the database
        # anyway.
        date = datetime.strptime(msg["datetime"], "%Y-%m-%d %H:%M:%S")
        status = int(msg["status"])
        elapsed = float(msg["elapsed"])

        sql = 'INSERT INTO '+self.table+'(datetime, status, elapsed, regex_found, error) VALUES(%s,%s, %s, %s, %s);'
        data = (date, status, elapsed, msg["regex_found"], msg["error"], )
        
        try:
            self.cursor.execute(sql, data)
            self.conn.commit()
        
        except Exception as e:
            log.log_error("Unable to execute query",e)

    def close(self):
        self.cursor.close()
        self.conn.close()




