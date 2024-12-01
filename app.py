import requests
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Imagga API credentials
API_KEY = 'acc_7cd04d07a4c6779'
API_SECRET = '3a86b52d13077b4417ed191880235c2b'
API_URL = 'https://api.imagga.com/v2/tags'

# Lista de URLs de imágenes
images = [
    "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Coral_Tree_Monsoon_Mallalli_Falls_Hassan_Jun24_A7CR_01575.jpg/750px-Coral_Tree_Monsoon_Mallalli_Falls_Hassan_Jun24_A7CR_01575.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/2/26/%2213_QR_CODE_ITA_LANG_-_Chianti_DOGC_wine_bottle_code_scan_smartphone_-_qr_code_steps.png"
]

@app.route('/')
def index():
    return render_template('index.html', images=images)

@app.route('/analyze', methods=['POST'])
def analyze():
    results = []
    
    # Recorrer cada imagen
    for image_url in request.form.getlist('images'):
        # Llamar al API de Imagga para obtener etiquetas
        response = requests.get(API_URL, auth=(API_KEY, API_SECRET), params={'image_url': image_url})
        data = response.json()
        
        # Obtener las etiquetas de la respuesta
        tags = data['result']['tags']
        
        # Ordenar las etiquetas por confianza (de mayor a menor)
        sorted_tags = sorted(tags, key=lambda x: x['confidence'], reverse=True)
        
        # Obtener solo las dos etiquetas más confiables
        top_tags = sorted_tags[:2]
        
        # Guardar los resultados
        results.append({
            'image': image_url,
            'tags': top_tags
        })

    # Pasar los resultados a la plantilla
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
