#Bot de Telegram de La Liga Española de Fútbol

[![Build Status](https://travis-ci.org/manuelalonsobraojos/proyectoIV.svg?branch=master)](https://travis-ci.org/manuelalonsobraojos/proyectoIV)

**Introducción**

El proyecto escogido para realizar a lo largo del curso en la asignatura de infraestructura virtual, es un bot de telegram.  
En concreto el bot será de la liga española de futbol, este bot mostrará información como puden ser los resultados de la jornada, la clasificación, el pichichi, etc.., todo ello dependiendo del comando que se use.

El bot será desarrollado en Python y será alojado junto con una base de datos en un servidor en la nube tales como **c9.io ó Amazon web services**. Se utilizarán dos servidores de base de datos, en uno guardaremos las IDs de los usuarios de telegram, y en otro servidor de base de datos será guardada la información que se le mostrará a los usuarios, una vez que la información haya sido obtenido mediante la tecnica de **Web Scraping** utilizando la libreria para python **BeautifulSoup**. 


**Testeo e Integración continua**

Como herramientas de construcción tengo un archivo Makefile y un requirements.txt. Con este archivo makefile podremos realizar la instalación de dependencias necescesarias para la ejecución de bot, ejecutar los test y ejecutar el bot. Todo ello con las siguientes ordenes respectivamente:  
- make install
- make test
- make ejecutar

Para la realización de los test he utilizado la libreria **unittest**, para su ejecución se ha incluido un objetivo *make test* dentro del archivo Makefile.

Como sistema de integración continua se utiliza Travis-CI, para ello he incluido un archivo .travis.yml en el repositorio, donde se configura la conexión con travis-ci y se le indica como instalar las dependencias necesarias para la ejecución del bot y como ejecutar los test.

**Despliegue en Heroku**

Para realizar el despliegue en Heroku, lo he configurado para cada que cada vez que haga push a el repositorio de github donde se encuentra el bot directamente se despliegue en heroku.

Para el despliegue haremos uso de un fichero **Procfile**, este fichero deberá de encontrarse en el directorio raíz y en el se declararán los comandos que deben ser ejecutados para arrancar el bot. El fichero quedaría asi:  
```
worker: cd bot_LaLiga && python bot_LaLiga.py 
```

Además del archivo Procfile es necesario un archivo con nombre **runtime.txt** en el que le especificaremos la versión de python que se está utilizando, en este caso la versión *python-2.7.12*.

Una vez tenemos esto vamos a la página de Heroku y hacemos clic en nueva aplicación y le ponemos el nombre que deseemos.  
Una vez creada la aplicación en Heroku, nos vamos a la configuración de despliegue y vinculamos la aplicación con el repositorio de github donde se encuentra el bot. Habilitaremos el despligue automático para que cada vez que hagamos un push a github se despliegue automáticamente, además de esto habilitaremos la opción de que solo se despligue si pasa los test de travis.

![img](https://github.com/manuelalonsobraojos/IV-Ejercicios/blob/master/Ejercicios-tema3/capturas/Captura.PNG)

Con respecto al servicio de base de datos, con respectos a los anteriores hitos la he pasado PostgreSQL, ya que es uno de los servicios de base de datos que nos ofrece Heroku gratuitamente. Para crear las tablas que necesitemos deberemos acceder a dicha base de datos con el comando ```heroku logs --tail --ps postgres --app <nombre de la app>```. 

Con esto ya tendremos configurado nuestro despliegue atomático y podremos probarlo desde telegram buscando el bot por el nombre de **@La_Liga_bot**. 

