import pymysql
import csv
try:
    with pymysql.connect(host = 'localhost',user='root',password='Kumbam@23',port=3306,database='accenture') as db:
        ############## inserting the record #####################         
        with open("realestate.csv","r") as fread:
            reader = csv.reader(fread)
            for record in reader:
                    #print(record)
                    street = record[0]
                    city = record[1]
                    #print(street,city)
                    query = "insert into stateinfo values('{}' ,'{}')"     
                    query = query.format(street,city)
                    db.execute(query)
                    print(db.rowcount , "record inserted")   
except pymysql.MySQLError as err:   
    print('Exception related to operation with MySQL')
    print(err)
except pymysql.DatabaseError as err:
    print('Database error')
    print(err)
except pymysql.OperationalError as err:
    print('Operational error')
    print(err)   
except Exception as err:
    print("Uknown error")
    print(err)