import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cdd2023",
    database="escolaturmad"
)
print(banco)

cursor=banco.cursor()
sql="delete from alunos where matricula = 6"
cursor.execute(sql)
banco.commit()
cursor.close()
banco.close()