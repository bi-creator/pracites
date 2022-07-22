import psycopg2


connection = psycopg2.connect(user="postgres",
                                  password="manjith",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="testing_psyco")

cur=connection.cursor()
# cur.execute("CREATE TABLE test(id serial PRIMARY KEY, sname CHAR(50), roll_num integer);")
# cur.execute("SELECT * from audit.dates_corrigendum_audit")
# r=cur.fetchall
connection.commit()
cur.execute("INSERT INTO test (id, sname, roll_num) \
      VALUES (110, 'Sara', 3)");

cur.execute("INSERT INTO test (id, sname, roll_num) \
      VALUES (120, 'Ema', 4)");

cur.execute("INSERT INTO test (id, sname, roll_num) \
      VALUES (330, 'Drabir', 2)");

cur.execute("INSERT INTO test (id, sname, roll_num) \
      VALUES (440, 'Surya', 1)");

connection.commit()
cur.execute("SELECT id, sname, roll_num from test")
print("ID   Roll No. Student Name")
print("--------------------------") 
rows = cur.fetchall()
for row in rows:
   print(row[0],' ',str(row[2]).strip(),'      ',row[1].strip())


print("after update")
cur.execute("UPDATE test set roll_num = 5 where ID=10")
cur.execute("UPDATE test set roll_num = 15 where ID=20")
cur.execute("UPDATE test set roll_num = 25 where ID=30")
cur.execute("UPDATE test set roll_num = 35 where ID=40")
cur.execute("UPDATE test set roll_num = 45 where ID=100")
connection.commit()
cur.execute("SELECT id, sname, roll_num from test")
print("ID   Roll No. Student Name")
print("--------------------------") 
rows = cur.fetchall()
for row in rows:
   print(row[0],' ',str(row[2]).strip(),'      ',row[1].strip())

print("after deletion")
cur.execute("DELETE from test where ID=10;")
cur.execute("DELETE from test where ID=20;")
cur.execute("DELETE from test where ID=30;")
cur.execute("DELETE from test where ID=40;")
connection.commit()
connection.close()