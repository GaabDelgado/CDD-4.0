import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cdd2023",
    database="escolaturmad"
)
print(banco)

nome1="Ricardo"
telefone1="81056664444"
cpf1="11111111111"
media1= 8.5
situação1="A"
FK_Turmas1='1'

cursor=banco.cursor()
sql="insert into alunos (nome, telefone, cpf,media,situação,Fk_Turmas) VALUES(%s,%s,%s,%s,%s,%s)"
data=(nome1,telefone1,cpf1,media1,situação1,FK_Turmas1)
cursor.execute(sql,data)
banco.commit()
userid=cursor.lastrowid
print(userid)
cursor.close()
banco.close()