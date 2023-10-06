import pyodbc as odbc
connectionString = (
r'DRIVER={ODBC Driver 17 for SQL Server};'
r'SERVER=MIS;'
r'DATABASE=qastore;'
r'Trusted_Connection=yes'
)
sqlStr="""INSERT INTO Student
(StudentID, FirstName, Surname, Course, City)
VALUES ('001', 'TestName', 'TestName', 'Maths', 'Leeds' ) 
SELECT * FROM Student"""
conn = odbc.connect(connectionString)
cur = conn.cursor()
cur.execute(sqlStr)
conn.commit()
conn.close()

#sqlStr="""CREATE TABLE Student (
#	StudentID int NOT NULL,
#	FirstName nvarchar(40) NOT NULL,
#	Surname   nvarchar(30) NULL,
#	Course nvarchar(30) NULL,
#	City nvarchar(15) NULL)"""
#conn = odbc.connect(connectionString)
#cur = conn.cursor() 
#cur.execute(sqlStr)
#conn.commit()
#conn.close()

