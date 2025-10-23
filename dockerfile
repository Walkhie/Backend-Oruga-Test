#Imagen base de Python
FROM python:3.11-slim

#Directorio de trabajo
WORKDIR /app

#Copiar dependencias y requisitos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto 
EXPOSE 8000

# Comando de arranque
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
