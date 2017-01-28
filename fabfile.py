from fabric.api import *
import os

def info_servidor():
    run ('uname -s')

def descargar():
    run ('sudo rm -rf proyectoIV')
    run ('sudo git clone https://github.com/manuelalonsobraojos/proyectoIV')

def iniciar():
    with shell_env(TOKEN=os.environ['TOKEN'], USER_BD=os.environ['USER_BD'], PASS_BD=os.environ['PASS_BD']):
        run ('sudo supervisorctl start La_Liga_bot')
    #run ('sudo python proyectoIV/bot_LaLiga/bot_LaLiga.py')

def detener():
    run ("sudo supervisorctl stop La_Liga_bot")

def borrar():
    run ('rm -rf proyectoIV')

def testear():
    with shell_env(TOKEN=os.environ['TOKEN'], USER_BD=os.environ['USER_BD'], PASS_BD=os.environ['PASS_BD']):
        run ('cd IV/ &&  python p_deportivas_bot/test_p_deportivas_bot.py')

def instalar():
    run ('cd proyectoIV && make bot_LaLiga/install')

def recargar():
    run("sudo supervisorctl reload")
