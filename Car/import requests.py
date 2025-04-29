import requests
from bs4 import BeautifulSoup
import os

# Fonction pour télécharger une image
def download_image(image_url, folder):
    # Si l'URL ne commence pas par http, ajouter l'URL de base
    if not image_url.startswith("http"):
        image_url = "https://docs.fivem.net" + image_url
    
    # Obtenir le contenu de l'image
    try:
        img_data = requests.get(image_url).content
        # Créer le nom du fichier à partir de l'URL
        file_name = os.path.join(folder, image_url.split("/")[-1])
        # Enregistrer l'image
        with open(file_name, 'wb') as handler:
            handler.write(img_data)
        print(f"Téléchargé : {file_name}")
    except Exception as e:
        print(f"Erreur lors du téléchargement de {image_url}: {e}")

# Fonction pour extraire les images .webp
def extract_webp_images(url, folder='C:\\Users\\s3r0o\\Desktop\\vehicle-webp'):
    # Créer le dossier pour les images si nécessaire
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Envoyer une requête pour obtenir le contenu du site
    response = requests.get(url)
    if response.status_code != 200:
        print("Erreur lors de la requête vers le site.")
        return
    
    # Parser le contenu HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Chercher toutes les balises <img> avec des images en .webp
    images = soup.find_all('img')
    for img in images:
        img_url = img.get('src')
        if img_url and img_url.endswith('.webp'):
            # Téléchargement de l'image .webp
            download_image(img_url, folder)

# URL du site que tu veux analyser
url = "https://docs.fivem.net/docs/game-references/vehicle-models/"
extract_webp_images(url)
