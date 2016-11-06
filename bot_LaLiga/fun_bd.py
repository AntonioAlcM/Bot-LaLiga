# -*- coding: utf-8 -*-
import os
import psycopg2


#DB_HOST = '127.0.0.1' 
#DB_USER = 'root' 
#DB_PASS = '123456' 
#DB_NAME = 'laliga'

#urlparse.uses_netloc.append("postgres")
#url = urlparse.urlparse(os.environ["postgres://dvrvjtupxbpjbs:enzqVLw1_CnTvtacmB2uFEzo16@ec2-54-247-189-242.eu-west-1.compute.amazonaws.com:5432/d8j7nr0lsdudmc"])

def run_query(query=''): 
	"""Funcion que ejecuta las consultas con la base de datos.

	   Parámetros:
		-query: consulta a la base de datos.

	"""
    	#datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
 	conn = psycopg2.connect(
	    database="d8j7nr0lsdudmc",
	    user="dvrvjtupxbpjbs",
	    password="enzqVLw1_CnTvtacmB2uFEzo16",
	    host="ec2-54-247-189-242.eu-west-1.compute.amazonaws.com",
	    port="5432"
	)
    	#conn = pymysql.connect(*datos) # Conectar a la base de datos 
    	cursor = conn.cursor()         # Crear un cursor 
    	cursor.execute(query)          # Ejecutar una consulta 
 
    	if query.upper().startswith('SELECT'): 
        	data = cursor.fetchall()   # Traer los resultados de un select 
    	else: 
        	conn.commit()              # Hacer efectiva la escritura de datos 
        	data = None 
 
    	cursor.close()                 # Cerrar el cursor 
    	conn.close()                   # Cerrar la conexión 
 
    	return data
    
def insertClasificacion(v_team,v_point,posicion):
	"""Funcion para insertar los datos de la clasificación en la base de datos.

	   Parámetros:
		-v_team: vector con los equipos.
		-v_point: vector con los puntos.
		-posicion: entero de la posición en liga 

	"""
    	query= "UPDATE clasificacion set equipo='%s',puntos='%s' where posicion=%i"% (v_team,v_point,posicion)
    	resultado=run_query(query)
    
    	return resultado

#devuelve la clasificación de la base de datos
def selectClasificacion():
	"""Funcion que devuelve la información de la clasificación de la base de datos.

	"""
    	query="SELECT* FROM clasificacion"
    	result = run_query(query)
    	return result

#Inserta en la base de datos los datos de los resultados de la jornada    
def insertResultados(v_local,v_result,v_visit,partido):
	"""Funcion para insertar los datos de los resultados de la jornada en la base de datos

	   Parámetros:
		-v_local: vector con los equipos locales.
		-v_result: vector con los resultados de los encuentros.
		-v_visit: vector con los equipos visitantes.
		-partido: entero que representa el número de partido 

	"""
	#query = "INSERT INTO clasificacion (posicion,Equipo) VALUES ('%i','%s')" % (i+1,v_team[i])
	query= "UPDATE resultados set local='%s',marcador='%s',visitante='%s' where partido=%i"% (v_local,v_result,v_visit,partido)
    	resultado=run_query(query)

#devuelve los resultadosde la base de datos
def selectResultados():
	"""Funcion que devuelve los equipos locales de los resultados de la jornada guardados en la base de datos.

	"""
    	query="SELECT local FROM resultados"
    	result = run_query(query)
    	return result

#devuelve los resultadosde la base de datos
def selectMarcador():
	"""Funcion que devuelve los marcadores de los resultados de la jornada guardados en la base de datos.

	"""
    	query="SELECT marcador FROM resultados"
    	result = run_query(query)
    	return result
    
#devuelve los resultadosde la base de datos
def selectVisitante():
	"""Funcion que devuelve los equipos visitantes de los resultados de la jornada guardados en la base de datos.

	"""
    	query="SELECT visitante FROM resultados"
    	result = run_query(query)
    	return result
