FROM ubuntu:14.04
#Primero de todo instalamos git
RUN apt-get -y update
RUN apt-get install -y git  
RUN cd /home && git clone https://github.com/manuelalonsobraojos/proyectoIV
#COPY ./ /home/proyectoIV
RUN cd /home/proyectoIV && chmod a+x docker_run
RUN cd /home/proyectoIV && ./docker_run
ENV TOKEN="263651123:AAHUqH6y-q2WCu5gkvKQ5PrrBhUKQ_9D0BU"
ENV USER_BD="dvrvjtupxbpjbs"
ENV PASS_BD="enzqVLw1_CnTvtacmB2uFEzo16"
CMD cd /home/proyectoIV && cd bot_LaLiga && python bot_LaLiga.py
