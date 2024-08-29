import os
import requests
from flask import Flask, jsonify
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Obtenez la clé API de l'environnement
rapidapi_key = os.getenv("RAPIDAPI_KEY")

app = Flask(__name__)

@app.route('/conjugate/<verb>', methods=['GET'])
def conjugate(verb):
    url = f"https://reverso-conjugator.p.rapidapi.com/conjugate?verb={verb}&language=fr"
    
    headers = {
        "x-rapidapi-key": rapidapi_key,
        "x-rapidapi-host": "reverso-conjugator.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to retrieve conjugation"}), response.status_code

# Lancer l'application Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
