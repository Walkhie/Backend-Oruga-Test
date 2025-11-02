## BACKEND CONTROL ORUGA
El proyecto corresponde al backend de una aplicación web para el control remoto del robot Oruga, desarrollado con FastAPI.
Su principal función es gestionar la comunicación entre la interfaz del usuario y el Orion Context Broker, actualizando dinámicamente el estado de la entidad correspondiente al robot según las órdenes de movimiento enviadas desde la aplicación.

De esta forma, el backend actúa como un intermediario inteligente que recibe las acciones del usuario (como avanzar, retroceder, girar, detenerse, etc.), las traduce en cambios de estado dentro del ecosistema FIWARE, y permite que el robot ejecute dichas instrucciones en tiempo real.


## Como correrlo 
### Comienzo rapido (cloud aws)
1. Iniciar una instancia EC2 (Recuerda abrir los puertos que vamos a utilizar)
2. Instalar dependencias (git y docker):
- sudo yum install 
- y git docker
3. Habilita y arranca docker:
- sudo systemctl enable docker
- sudo systemctl start docker
4. Instala docker compose (procura instalar la version más reciente)
5. Clona el repositorio
- git clone https://github.com/Walkhie/Backend-Oruga-Test.git
6. Entra a la carpeta y lanza los 3 servicios (FASTAPI, ORION, MONGODB):
- docker compose up -d --build
