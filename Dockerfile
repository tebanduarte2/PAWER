# Usa una imagen ligera de Python
FROM python:3.11-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia dependencias e instálalas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends gettext && rm -rf /var/lib/apt/lists/*

# Copia todo el proyecto
COPY . .

# Recoge archivos estáticos
RUN python manage.py collectstatic --noinput

# Expón el puerto 80
EXPOSE 80

# Ejecuta la app con gunicorn (usa whitenoise para estáticos)
CMD ["gunicorn", "Pawer.wsgi:application", "--bind", "0.0.0.0:80"]
