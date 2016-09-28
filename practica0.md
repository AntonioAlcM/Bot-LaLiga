# Práctica 0

### 1-Creación de clave pública y añadido a github
Para crear la clave pública otilizaremos el siguiente comando: 
```
ssh-keygen -t rsa -C "manuelalonso136@gmail.com"
```
![img](https://github.com/manuelalonsobraojos/proyectoIV/blob/rama0/capturas/Captura1.PNG)

Una vez hemos creado la clave pública la copiamos del archivo **~/.ssh/id_rsa.pub**, para ello utilizaremos la herramiente **xclip** ejecutando el siguiente comando:
```
xclip -sel clip < ~/.ssh/id_rsa.pub
```
Una vez tenemos copiada la clave nos dirigimos a <github.com> y accedemos al apartado **Settings** y dentro de este apartado accedemos a la pestaña **SSH and GPG keys** en la que añadiremos la clave copiada anteriormente.  

![img](https://github.com/manuelalonsobraojos/proyectoIV/blob/rama0/capturas/Captura2.PNG)


### 2-Configuración de nombre y dirección de correo electrónico
Establecer el nombre de usuario y la dirección de correo electrónico es importante para que aparezcan en los **commits**. Para ello utilizaremos los siguientes comandos:
```
$ git config --global user.name "manuelalonsobraojos"
$ git config --global user.email manuelalonso136@gmail.com
```

### 3-Creamos hitos e issures
Creamos un hito que será la entrega de la práctica 0.  
![img](https://github.com/manuelalonsobraojos/proyectoIV/blob/rama0/capturas/Captura4.PNG)  

Tambien crearemos dos issures que serán actualizar el README y otro para subir el archivo .gitignore.  

Una vez creadas las tareas clonaremos el repositorio a nuestro PC como vemos en la siguiente imagen.  
![img](https://github.com/manuelalonsobraojos/proyectoIV/blob/rama0/capturas/Captura3.PNG)

Para llevar acabo estas tareas deberemos hacer los siguiente:  
```
$git add .
$git commit -m "Actualizando README.md y subiendo .gitignore close #1 close #2"
$git push
```
![img](https://github.com/manuelalonsobraojos/proyectoIV/blob/rama0/capturas/Captura5.PNG)

### 4-Creamos Nueva Rama
Crearemos una nueva rama para la entrega de la práctica 0. Para crear y saltarnos a la nueva rama utilizaremos el comando:
```
$ git checkout -b rama0
```
Y hacemos un push a la nueva rama 

```
$ git push origin rama0
```
Una vez hecho esto solo nos bastará con subir el archivo de la práctica 0.

