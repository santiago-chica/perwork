FROM python:3.11 

ADD main.py .

COPY requirements.txt .
RUN pip install -r ./requirements.txt


RUN apt-get update && \
apt-get install -y --no-install-recommends texlive-latex-recommended texlive-fonts-recommended && \
apt-get install -y --no-install-recommends texlive-latex-extra texlive-fonts-extra texlive-lang-all && \
rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]