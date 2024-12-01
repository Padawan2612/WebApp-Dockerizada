# Usa una imagen base de Python
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Instalar dependencias
RUN pip install -r requirements.txt

# Establecer las claves de Imagga directamente como variables de entorno
ENV IMAGGA_API_KEY="acc_7cd04d07a4c6779"
ENV IMAGGA_API_SECRET="3a86b52d13077b4417ed191880235c2b"

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]
