import mysql.connector as mysql

# connecting to the database using 'connect()' method
# it takes 3 required parameters 'host', 'user', 'passwd'


def userinfo(Name, Mobile_number, Email, Age, Time):
    db = mysql.connect(
        host="localhost", 
        user="root",
        passwd="Advitiya@1234",
        database="rasabot"
    )

    cursor = db.cursor()
    sql="CREATE TABLE patient_info (Name VARCAR(25), Mobile_number VARCAR(10), Email VARCAR(20), Age VARCAR(4), Time VARCAR(15));"
   # sql = 'insert into user_details (Name, Mobile_number, Email, Age, Time) values ("{0}","{1}", "{2}", "{3}", "{4}");'.format(Name, Mobile_number, Email, Age, Time)
    cursor.execute(sql)
    db.commit()