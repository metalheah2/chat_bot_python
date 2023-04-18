'''
	Libreria sqlite3 : pip install sqlite3 
	Autor : Marco Jhoel Churata Torres.
	Titulo : base_datos.py
'''

import sqlite3

conn=sqlite3.connect('base_chat.db')
c=conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS Negocio(Cliente TEXT,Telefono TEXT ,Correo TEXT,Direccion TEXT,Servicio TEXT,Lugar TEXT,Empleados TEXT,Horario TEXT,Mercancia TEXT)")

def create_table_2():
	c.execute("CREATE TABLE IF NOT EXISTS Vivienda(Cliente TEXT,Telefono TEXT ,Correo TEXT,Direccion TEXT,Servicio TEXT,Lugar TEXT,Tipo TEXT,Acceso_1 TEXT,Acceso_2 TEXT)")
	
def data_entry():
	c.execute("INSERT INTO Negocio VALUES('uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve')")
	conn.commit()
	
	c.close()
	conn.close()

	
create_table()
create_table_2()
data_entry()