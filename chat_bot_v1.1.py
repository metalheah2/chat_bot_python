'''
	Libreria sqlite3 : pip install sqlite3 
	Autor : Marco Jhoel Churata Torres.
	Titulo : chat_bot_v1.1.py
'''

import sqlite3

conn=sqlite3.connect('base_chat.db')
c=conn.cursor()

def data_entry(lugar,cliente,cliente_telf,cliente_correo,cliente_dir,dato_1,dato_2,dato_3,dato_4,dato_5):
	data=("'"+cliente+"',"+"'"+cliente_telf+"',"+"'"+cliente_correo+"',"+
		"'"+cliente_dir+"',"+"'"+dato_1+"',"+"'"+dato_2+"',"+"'"+dato_3+"',"+
		"'"+dato_4+"',"+"'"+dato_5+"'")
	
	try:
		c.execute("INSERT INTO "+lugar+" VALUES("+data+")")
		conn.commit()
		c.close()
		conn.close()
		print("Le enviaremos un WhatsApp para comunicarnos con usted ,GRACIAS ¡¡¡")
	except:
		print("Ocurrio un error.")

def registro_cliente():
	print("Para guardar tu proyecto de seguridad necesitamos tus datos:")
	numero_telf=input("Celular : ")
	correo=input("Correo electronico : ")
	direccion=input("Direccion : ")
	datos_cliente=("Celular : "+numero_telf+"Correo electronico : "+correo+"Direccion : "+direccion)
	return numero_telf,correo,direccion

def vivienda_negocio(lugar_1):
	if(lugar_1=="1"):
		print('''¿Cómo es tu vivienda?
		
	1) Piso
	2) Chalet''')
		lugar_2=input()
		if(lugar_2=="1"):
			opc_1="Vivienda-Piso"
			return opc_1
		if(lugar_2=="2"):
			opc_2="Vivienda-Chalet"
			return opc_2
		else:
			print("Respuesta Incorrecta.")
			return "Respuesta Incorrecta."
	if(lugar_1=="2"):
		print('''¿Dónde se encuentra el negocio o empresa?
	
	1) Dentro del núcleo urbano
	2) Fuera del nucleo urbano''')
		lugar_2=input()
		if(lugar_2=="1"):
			opc_1="Negocio-Dentro del nucleo urbano"
			return opc_1
		if(lugar_2=="2"):
			opc_2="Negocio-Fuera del nucleo urbano"
			return opc_2
		else:
			print("Respuesta Incorrecta.")
			return "Respuesta Incorrecta."
	else:
		print("Respuesta Incorrecta.")
		return "Respuesta Incorrecta."

def vivienda_tipo():
	print('''¿Cómo es tu vivienda?
	
	1) Departamento
	2) Casa
''')
	opcion1=input()
	if(opcion1=="1"):
		opc_1="Departamento"
		return opc_1
	if(opcion1=="2"):
		opc_2="Casa"
		return opc_2
	else:
		return opcion1

def vivienda_acceso1():
	print('''¿Cómo es el acceso principal de la vivienda?
	
	1) Portal a pie de calle
	2) Urbanización no vigilada
	3) Urbanización vigilada''')
	opcion1=input()
	if(opcion1=="1"):
		opc_1="Portal a pie de calle"
		return opc_1
	if(opcion1=="2"):
		opc_2="Urbanización no vigilada"
		return opc_2
	if(opcion1=="3"):
		opc_3="Urbanización vigilada"
		return opc_3
	else:
		return opcion1

def vivienda_acceso2():
	print('''¿La vivienda tiene accesos secundarios?
	
	1) Jardín o parcela
	2) Balcón o Terraza
	3) No tiene''')
	opcion1=input()
	if(opcion1=="1"):
		opc_1="Jardín o parcela"
		return opc_1
	if(opcion1=="2"):
		opc_2="Balcón o Terraza"
		return opc_2
	if(opcion1=="3"):
		opc_3="No tiene"
		return opc_3
	else:
		return opcion1
		
def negocio_empleados():
	print('''¿Cuántos empleados tiene?
	
	1) Solo yo
	2) De 2 a 5 empleados
	3) Más de 5 empleados''')
	opcion1=input()
	if(opcion1=="1"):
		opc_1="Solo yo"
		return opc_1
	if(opcion1=="2"):
		opc_2="De 2 a 5 empleados"
		return opc_2
	if(opcion1=="3"):
		opc_3="Más de 5 empleados"
		return opc_3
	else:
		return opcion1
		
def negocio_horario():
	print('''¿Qué horario tiene tu negocio?
	
	1) Solo mañanas
	2) Solo tardes
	3) Mañanas y tardes
	4) Nocturno
	5) 24 horas''')
	opcion1=input()
	if(opcion1=="1"):
		opc_1="Solo mañanas"
		return opc_1
	if(opcion1=="2"):
		opc_2="Solo tardes"
		return opc_2
	if(opcion1=="3"):
		opc_3="Mañanas y tardes"
		return opc_3	
	if(opcion1=="4"):
		opc_4="Nocturno"
		return opc_4
	if(opcion1=="5"):
		opc_5="24 horas"
		return opc_5
	else:
		return opcion1
		
def negocio_mercancia():
	print('''¿Qué tipo de mercancía tienes es tu negocio?
	
	1) Gran valor
	2) Medio valor
	3) Bajo valor''')
	opcion1=input()
	if(opcion1=="1"):
		opc_1="Gran valor"
		return opc_1
	if(opcion1=="2"):
		opc_2="Medio valor"
		return opc_2
	if(opcion1=="3"):
		opc_3="Bajo valor"
		return opc_3
	else:
		return opcion1
		
#************************************ Inicio ***********************************
		
print("Hola ¡¡¡ \nComo te llamas ?")
cliente=input()
print("Mucho gusto "+cliente+" ¡¡¡")
print('''\nSoy Marco Jhoel,estudiante de Ingenieria Electronica y Telecomunicaciones 
\nLos servicios que ofresco son:
 Venta e Instalacion:
  1)Alarmas de intrusión
  2)Video Porteros e Intercomunicadores
  3)Control de acceso y asistencia
  4)Redes y Telecomunicaciones
  5)Camaras de Seguridad
  6)Asesoria venta e instalacion
  
Dime con que opcion te ayudo :D
''')

dato_1=input()

#*********************************** Alarmas_de_intrusión ***********************************************

if(dato_1=="1"):
	print('''Las alarmas de intrusión son, en lineas generales,aquellas cuyo cometido es detectar y alertar de la presencia de intrusos dentro de su radio de acción.
Pueden instalarse tanto en negocios como en viviendas particulares,fincas de vecinos,oficinas,almacenes,fábricas... y resultan de una gran utilidad si lo que buscas es garantizar la seguridad.

¿La alarma es para una vivienda o un negocio ?

	1)Vivienda
	2)Negocio
''')
	dato_1="Alarmas_de_intrusión"
	lugar_1=input()
	dato_2=(vivienda_negocio(lugar_1))
	
	if(dato_2=="Vivienda-Piso" or dato_2=="Vivienda-Chalet"):
		lugar="Vivienda"
		dato_3=vivienda_tipo()
		dato_4=vivienda_acceso1()
		dato_5=vivienda_acceso2()
		cliente_telf,cliente_correo,cliente_dir=registro_cliente()
		data_entry(lugar,cliente,cliente_telf,cliente_correo,cliente_dir,dato_1,dato_2,dato_3,dato_4,dato_5)
		
	if(dato_2=="Negocio-Dentro del nucleo urbano" or dato_2=="Negocio-Fuera del nucleo urbano"):
		lugar="Negocio"
		dato_3=negocio_empleados()
		dato_4=negocio_horario()
		dato_5=negocio_mercancia()
		cliente_telf,cliente_correo,cliente_dir=registro_cliente()
		data_entry(lugar,cliente,cliente_telf,cliente_correo,cliente_dir,dato_1,dato_2,dato_3,dato_4,dato_5)
		
		
#************************* Intercomunicadores y Videoporteros ************************************
	
if(dato_1=="2"):
	print('''Con el avance del IoT los sistemas de intercomunicadores y videoporteros han cobrado importancia en las aplicaciones de seguridad y control de acceso tanto en hogares como en el sector corporativo e industrial.

¿El sistema es para una vivienda o un negocio ?

	1)Vivienda
	2)Negocio''')
	
	dato_1="Video_Porteros_ó_Intercomunicadores"
	lugar_1=input()
	dato_2=(vivienda_negocio(lugar_1))
	
	if(dato_2=="Vivienda-Piso" or dato_2=="Vivienda-Chalet"):
		lugar="Vivienda"
		dato_3=vivienda_tipo()
		dato_4=vivienda_acceso1()
		dato_5=vivienda_acceso2()
		cliente_telf,cliente_correo,cliente_dir=registro_cliente()
		data_entry(lugar,cliente,cliente_telf,cliente_correo,cliente_dir,dato_1,dato_2,dato_3,dato_4,dato_5)
		
		
	if(dato_2=="Negocio-Dentro del nucleo urbano" or dato_2=="Negocio-Fuera del nucleo urbano"):
		lugar="Negocio"
		dato_3=negocio_empleados()
		dato_4=negocio_horario()
		dato_5=negocio_mercancia()
		cliente_telf,cliente_correo,cliente_dir=registro_cliente()
		data_entry(lugar,cliente,cliente_telf,cliente_correo,cliente_dir,dato_1,dato_2,dato_3,dato_4,dato_5)
		

#******************************** Control de acceso y asistencia ************************************
		
if(dato_1=="3"):
	print('''Los controles de acceso y asistencia son sistemas que, una vez que identifique al usuario, permite o niega el acceso a un recurso. Este recurso puede ser un servicio, habitación, datos, recinto y equipos de una empresa. A su vez, gestionan y registran las horas de entrada y salida de los trabajadores y visitantes.''')
	
	dato_1="Control_de_acceso_y_asistencia"
	dato_2=(vivienda_negocio("2"))
	
	lugar="Negocio"
	dato_3=negocio_empleados()
	dato_4=negocio_horario()
	dato_5=negocio_mercancia()
	cliente_telf,cliente_correo,cliente_dir=registro_cliente()
	data_entry(lugar,cliente,cliente_telf,cliente_correo,cliente_dir,dato_1,dato_2,dato_3,dato_4,dato_5)
	

#*************************************** Redes y Telecomunicaciones	*********************************
	
if(dato_1=="4"):
	print('''Las instalaciones de telecomunicaciones incluyen a las redes informáticas, las cuales son aquellos equipos que transmiten información. Generalmente lo hacen a través de señales electromagnéticas. Estas pueden emitir el comunicado en forma de datos de audio, video, entre otros.

¿El sistema es para una vivienda o un negocio ?

	1)Vivienda
	2)Negocio''')
	
	dato_1="Redes_y_Telecomunicaciones"
	lugar_1=input()
	dato_2=(vivienda_negocio(lugar_1))
	
	if(dato_2=="Vivienda-Piso" or dato_2=="Vivienda-Chalet"):
		lugar="Vivienda"
		dato_3=vivienda_tipo()
		dato_4=vivienda_acceso1()
		dato_5=vivienda_acceso2()
		cliente_telf,cliente_correo,cliente_dir=registro_cliente()
		data_entry(lugar,cliente,cliente_telf,cliente_correo,cliente_dir,dato_1,dato_2,dato_3,dato_4,dato_5)
		
		
	if(dato_2=="Negocio-Dentro del nucleo urbano" or dato_2=="Negocio-Fuera del nucleo urbano"):
		lugar="Negocio"
		dato_3=negocio_empleados()
		dato_4=negocio_horario()
		dato_5=negocio_mercancia()
		cliente_telf,cliente_correo,cliente_dir=registro_cliente()
		data_entry(lugar,cliente,cliente_telf,cliente_correo,cliente_dir,dato_1,dato_2,dato_3,dato_4,dato_5)

#***************************************** Camaras de Seguridad **************************************
		
if(dato_1=="5"):
	print('''La cámara de seguridad sirve para monitorear y tener un registro de las actividades de las personas en una vivienda o negocio. La cámara de vigilancia puede estar oculta en el interior de la vivienda o instalada al aire libre y permite recopilar pruebas de posibles delitos o robos.

¿El sistema es para una vivienda o un negocio ?

	1)Vivienda
	2)Negocio''')
	
	dato_1="Camaras_de_Seguridad"
	lugar_1=input()
	dato_2=(vivienda_negocio(lugar_1))
	
	if(dato_2=="Vivienda-Piso" or dato_2=="Vivienda-Chalet"):
		lugar="Vivienda"
		dato_3=vivienda_tipo()
		dato_4=vivienda_acceso1()
		dato_5=vivienda_acceso2()
		cliente_telf,cliente_correo,cliente_dir=registro_cliente()
		data_entry(lugar,cliente,cliente_telf,cliente_correo,cliente_dir,dato_1,dato_2,dato_3,dato_4,dato_5)
		
		
	if(dato_2=="Negocio-Dentro del nucleo urbano" or dato_2=="Negocio-Fuera del nucleo urbano"):
		lugar="Negocio"
		dato_3=negocio_empleados()
		dato_4=negocio_horario()
		dato_5=negocio_mercancia()
		cliente_telf,cliente_correo,cliente_dir=registro_cliente()
		data_entry(lugar,cliente,cliente_telf,cliente_correo,cliente_dir,dato_1,dato_2,dato_3,dato_4,dato_5)
