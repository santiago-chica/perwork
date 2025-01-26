# Usa la imagen base de Debian Bookworm
FROM debian:bookworm

# Metadatos
LABEL maintainer="Julian Didier (theredfish)" \
      description="A docker image based on Debian that provides pdflatex, Python, and Flask for PyLaTeX" \
      repo="https://github.com/theredfish/docker-pdflatex"

# Instala dependencias del sistema (TeX Live y Python)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-lang-all \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Configura el entorno de Python
RUN python3 -m pip install --upgrade pip

# Copia los archivos de tu aplicación
COPY . /app
WORKDIR /app

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python3", "app.py"]
