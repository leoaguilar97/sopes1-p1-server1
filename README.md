# Proyecto #1 - SISTEMAS OPERATIVOS 1

## SERVIDOR 1:
En este servidor se ejecutará una API REST dentro de un contenedor de Docker. 

Su funcionamiento será similar al de un balanceador de carga. 

Cuando reciba la petición POST del balanceador de carga este debe elegir el servidor al que mandará el elemento, 
consultará el porcentaje de RAM, de CPU y la cantidad de elementos almacenados en A y B. 

Tomando en cuenta los siguientes criterios:

* Si la base de datos de A tiene más elementos que B, se insertará en B, en caso contrario se insertará en A.
* Si ambos tienen la misma cantidad de elementos almacenados, se comparará el porcentaje de RAM utilizada, el servidor con menor porcentaje será el escogido.
* Si ambos tienen el mismo porcentaje de RAM, debe realizarse la comparación con el porcentaje de CPU.
* Si el porcentaje de CPU es el mismo, debe enviarse al Servidor A.

## LINKS UTILIZADOS

https://www.metricfire.com/blog/develop-and-deploy-a-python-api-with-kubernetes-and-docker/

https://docs.docker.com/engine/install/ubuntu/

https://hub.docker.com/_/python/

https://realpython.com/python-versions-docker/

