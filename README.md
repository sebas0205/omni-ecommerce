# Prueba OmniLatam

## Descripción
El reto consiste en crear una api donde se pueda ralizar el flujo basico de un e-commerce.

## Implementación

La solucion se desarrollo  utilizando :
- Python 3.8.
- Django=3.2.5
- djangorestframework=3.12.4
- MySql ( AWS RDS).


## Ejecución

Para iniciar el servicio se debe ejecutar :
```
java -jar mutants.jar
```
Los servicios estan expuestos y se pueden ver por medio de Swagger en la url :

http://127.0.0.1:8000/api/schema/swagger-ui/


## Modelo ER

El modelo ER creado  para la solución es el siguiente :

<p align="center"> 
  <img src="diagrama-ER.png">
</p>

## Coverage

Para realizar el coverage se utilizó covergage.py , obteniendo un porcentage del 92%
La información sobre el coverage puede ser encontrada en la carpeta [acá](htmlcov)



