from fabric.api import *

def descargar():
    run ('sudo rm -rf proyectoIV')
    run ('sudo git clone https://github.com/manuelalonsobraojos/proyectoIV')

def iniciar():
    run ('sudo python proyectoIV/bot_LaLiga/bot_LaLiga.py')

def detener():
    run ('kill -9 $(pidof python)')

def borrar():
    run ('rm -rf proyectoIV')

def testear():
    run ('cd proyectoIV && make test')

def instalar():
    run ('cd proyectoIV && make install')
