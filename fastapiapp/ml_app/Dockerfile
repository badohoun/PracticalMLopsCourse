FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7



# Copie des fichiers 

COPY app.py app.py
COPY models/gender_vectorizer.pkl  models/gender_vectorizer.pkl
COPY models/gender_nv_model.pkl  models/gender_nv_model.pkl



RUN pip3 install --no-cache-dir fastapi
RUN pip3 install --no-cache-dir uvicorn
RUN pip3 install --no-cache-dir joblib 
RUN pip3 install --no-cache-dir scikit-learn==0.24.1 


# On ouvre et expose le port 6000
EXPOSE 80

# Lancement de l'API
# Attention : ne pas lancer en daemon ! (bloquant: faut jamais exécuter l'application en arrière plan , il faut laisser l'application en suspens)
CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "80"]

