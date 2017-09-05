# -*- coding: utf-8 -*-

import telebot 
from telebot import types 
from telebot import util
import time # Librería para hacer que el programa que controla el bot no se acabe.
import funciones
import os

TOKEN = os.environ['TOKEN'] # Nuestro tokken del bot (el que @BotFather nos dió).
bot = telebot.TeleBot(TOKEN)

funciones.recolectData()
funciones.inserDataResult()

#############################################
# log                                       #
#############################################
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
	for m in messages: # Por cada dato 'm' en el dato 'messages'
        	if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
			cid = m.chat.id # Almacenaremos el ID de la conversación.
		    	print ("[" + str(cid) + "]: " + m.text) # Y haremos que imprima algo parecido a esto -> [52033876]: /start

bot.set_update_listener(listener)

@bot.message_handler(commands=['clasificacion1']) 
def clasificacion(m): # Definimos una función que resuelva lo que necesitemos.
	"""Funcion que envia la clasificiación de la liga española al id que ha realizado la petición. 

	   Parámetros:
		-m:id de la conversación 

	"""
	funciones.recolectData()
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	mensaje=funciones.selectDataClasi()
	bot.send_message( cid, mensaje)


bot.set_update_listener(listener)
@bot.message_handler(commands=['resultados1']) 
def resultados(m): # Definimos una función que resuelva lo que necesitemos.
	"""Funcion que envia los resultados de la jornada al id que ha realizado la petición. 

	   Parámetros:
		-m:id de la conversación 

	"""

	funciones.inserDataResult()
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	mensaje=funciones.selectDataResult()
	bot.send_message( cid, mensaje)


bot.set_update_listener(listener)
@bot.message_handler(commands=['clasificacion2']) 
def clasificacion2(m): # Definimos una función que resuelva lo que necesitemos.
	"""Funcion que envia la clasificiación de la liga de 2ª division española al id que ha realizado la petición. 

	   Parámetros:
		-m:id de la conversación 

	"""
	funciones.recolectDataSegunda()
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	mensaje=funciones.selectDataClasiSeg()
	bot.send_message( cid, mensaje)


bot.set_update_listener(listener)
@bot.message_handler(commands=['resultados2']) 
def resultados2(m): # Definimos una función que resuelva lo que necesitemos.
	"""Funcion que envia los resultados de la jornada al id que ha realizado la petición. 

	   Parámetros:
		-m:id de la conversación 

	"""

	funciones.inserDataResultSegunda()
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	mensaje=funciones.selectDataResultSegunda()
	bot.send_message( cid, mensaje)

bot.polling(none_stop=True)
