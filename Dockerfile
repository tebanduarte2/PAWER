# Usa una imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del proyecto
COPY . .

# Expón el puerto 8000
EXPOSE 8000

# Comando para ejecutar gunicorn con Django
CMD ["gunicorn", "Pawer.wsgi:application", "--bind", "0.0.0.0:8000"]
