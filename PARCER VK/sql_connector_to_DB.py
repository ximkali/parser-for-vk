import mysql
import mysql.connector
from mysql.connector import errorcode

try:
    mydb = mysql.connector.connect(     host="127.0.0.1",   user="root",    password="first_korneplod", database ="dimas" )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


id = -12564
is_bot = 1





curs = mydb.cursor()

curs.callproc("sozdanie_polzovatelei", [id,is_bot,0,0] )
mysql.connector.commit()   




