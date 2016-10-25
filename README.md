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
