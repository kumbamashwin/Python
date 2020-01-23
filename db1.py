
import pymysql


try:
    with pymysql.connect(host = 'localhost',user='root',password='Kumbam@23',port=3306,database='accenture') as db:
        ############# display the records ###################
        query = "select * from stateinfo"
        db.execute(query)
        for record in db.fetchall():
            ## every record is a tuple 
            print("Street :", record[0])
            print("City   :", record[1])
            print("------------")
        ############## inserting the record #####################
        query = "insert into stateinfo values('{}' ,'{}')"        
        db.execute(query.format('101 GT Road','Chennai') )
        db.execute(query.format('Attapur','Mehdipatnam') )
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