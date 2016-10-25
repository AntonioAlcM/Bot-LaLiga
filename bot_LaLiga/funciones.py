# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import fun_bd
import re

requests.packages.urllib3.disable_warnings()

def recolectData():
	"""Funcion que scrapea de la web la información de la clasificación de la liga española de fútbol.

	"""
    	url = "http://resultados.as.com/resultados/futbol/primera/clasificacion/"
	#cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	
	# Realizamos la petición a la web
    	req = requests.get(url)

	# Comprobamos que la petición nos devuelve un Status Code = 200
    	statusCode = req.status_code
    	if statusCode == 200:

		# Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
		html = BeautifulSoup(req.text,"html.parser")
	    	# Obtenemos todos los divs donde estan las entradas
		entradas = html.find_all('span', {'class' : 'nombre-equipo'})
		puntos = html.find_all('td', {'class' : 'destacado'})
		v_point=[]
		for i,info in enumerate(puntos):
			if i<20:
				v_point.insert(i, info.text)
				
		# Recorremos todas las entradas para extraer el título, autor y fecha
		v_team=[]
		for i,entrada in enumerate(entradas):
			# Con el método "getText()" no nos devuelve el HTML
			# Sino llamamos al método "getText()" nos devuelve también el HTML
			if i<20:
				v_team.insert(i, entrada.text)				

		
		for i in range(len(v_team)):
			fun_bd.insertClasificacion(v_team[i],v_point[i],i+1)
			
		
    	else:
		print "Status Code %d" %statusCode
	    

def selectDataClasi():
	"""Funcion que obtiene los datos de la clasificación guardados en la base de datos y los convierte en un string para su posterior envio.

	"""
	result=fun_bd.selectClasificacion()
	
	msn=[]
	for i,element in enumerate(result):
		msn.insert(i,list(element))
	
	msn2=""
	
	for i in msn:
		msn2+=str(i)+ " pts" + "\n"
	
	msn3=""
	for i in msn2:
		if ord(i)!=92:
			msn3+=i
			
	msn2=msn3
	msn2=msn2.replace("[","")
	msn2=msn2.replace("]","")
	msn2=msn2.replace("'","")
	msn2=msn2.replace("L,","-")
	msn2=msn2.replace(",","")
	msn2=msn2.replace("xe9","é")
	msn2=msn2.replace("xe1","á")
	
	return msn2
	
def inserDataResult():
	"""Funcion que scrapea de la web la información de los resultados de la jornada de la liga española de fútbol.

	"""
	url = "http://resultados.as.com/resultados/futbol/primera/jornada/"


	req = requests.get(url)
	
	v_tlocal=[] #vector equipos locales
	v_tvisit=[] #vector equipos visitantes
	v_result=[] #vector resultados
	v_fecha=[]  #vecto fechas
	
	statusCode = req.status_code
	if statusCode == 200:
	
		# Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
	    	html = BeautifulSoup(req.text,"html.parser")
	
	    	# Obtenemos todos los divs donde estan las entradas de los equipos locales
		entradas = html.find_all('div',{'class':'equipo-local'})
		for i,entrada in enumerate(entradas):
			equipo_local = entrada.find('span', {'class' : 'nombre-equipo'}).getText()
			v_tlocal.insert(i, equipo_local)		
	
		# Obtenemos todos los divs donde estan las entradas de los equipos visitantes
		entradas2 = html.find_all('div',{'class':'equipo-visitante'})
		for i,entrada in enumerate(entradas2):
			equipo_visit = entrada.find('span', {'class' : 'nombre-equipo'}).getText()
			v_tvisit.insert(i, equipo_visit)
	
		# Obtenemos todos los divs donde estan los resultados finalizados
		entradas3=html.find_all('a', {'class' : 'resultado'})
		for i,entrada in enumerate(entradas3):
			#resultado = entrada.find('a', {'class' : 'resultado'}).getText()
			v_result.insert(i, entrada.text)
		
		if len(v_result)<10:
			for i in range(len(v_result),10):
				v_result.insert(i,"-")
	
		# Obtenemos todos los divs donde estan las fechas
		entradas4=html.find_all('span', {'class' : 'fecha'})
		for i,entrada in enumerate(entradas4):
			#resultado = entrada.find('a', {'class' : 'resultado'}).getText()
			v_fecha.insert(i, entrada.text)
	
		#print (entradas)
	
		for i in range(10):
			fun_bd.insertResultados(v_tlocal[i],v_result[i],v_tvisit[i],i+1)
		
	else:
	    	print "Status Code %d" %statusCode
	    	
	
def selectDataResult():
	"""Funcion que obtiene los datos de los resultados guardados en la base de datos y los convierte en un string para su posterior envio.

	"""
	result=fun_bd.selectResultados()
	result1=fun_bd.selectMarcador()
	result2=fun_bd.selectVisitante()
	
	msn=[]
	for i,element in enumerate(result):
		msn.insert(i,list(element))
	
	msn1=[]
	for i,element in enumerate(result1):
		msn1.insert(i,list(element))
		
	msn4=[]
	for i,element in enumerate(result2):
		msn4.insert(i,list(element))
	
	msn2=""
	
	for i in range(10):
		msn2+=re.sub(r'\s', '',str(msn[i])+ str(msn1[i])+str(msn4[i]))+"\n"
	
	msn3=""
	for i in msn2:
		if ord(i)!=92:
			msn3+=i
		
	msn2=msn3
	msn2=msn2.replace("[","")
	msn2=msn2.replace("]","")
	msn2=msn2.replace("'","")
	msn2=msn2.replace("L,","-")
	msn2=msn2.replace(",","")
	msn2=msn2.replace("xe9","é")
	msn2=msn2.replace("xe1","á")

	return msn2
	
