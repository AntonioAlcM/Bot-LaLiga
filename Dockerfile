FROM ubuntu
RUN apt-get install -y git  #Primero de todo instalamos git
RUN cd /home && git clone https://github.com/manuelalonsobraojos/proyectoIV
#COPY ./ /home/proyectoIV
RUN cd /home/proyectoIV && chmod a+x docker_run
RUN cd /home/proyectoIV && ./docker_run
CMD cd /home/proyectoIV && make ejecutar
