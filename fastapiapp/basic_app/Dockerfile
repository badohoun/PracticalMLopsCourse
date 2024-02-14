# Image de base de quelques megas : a part du linux il y'a quasiment rien dessus 
from alpine:3.11

# Installation de Python 3 and pip3 avec des gestionnaires de paquets avec du no cache : ne pas conserver tous les fichiers temporaires : économiser des dizaines de mega octets 
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools 


# Mise à jour de pip3
RUN pip3 install --upgrade pip 


RUN mkdir /app
WORKDIR /app


# Copie des fichiers 

COPY app.py app.py

RUN pip3 install --no-cache-dir fastapi
RUN pip3 install --no-cache-dir uvicorn 

# On ouvre et expose le port 5000
EXPOSE 8000

# Lancement de l'API
# Attention : ne pas lancer en daemon ! (bloquant: faut jamais exécuter l'application en arrière plan , il faut laisser l'application en suspens)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
