import pymysql
from configparser import ConfigParser

parser = ConfigParser() 
parser.read('properties.conf')
username = parser.get('database_config', 'username')
password = parser.get('database_config', 'password')
hostname = parser.get('database_config', 'hostname')
port = parser.get('database_config', 'port')
database = parser.get('database_config','database')


try:
    with pymysql.connect(host = hostname,user=username,password=password ,port=int(port),database=database) as db:
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