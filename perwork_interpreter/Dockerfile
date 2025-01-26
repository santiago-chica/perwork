
# Instala TeX Live (pdfLaTeX)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expone el puerto en el que corre Flask
EXPOSE 5000

