# config.py - Paramètres du projet Stable Diffusion

# Modèle Stable Diffusion fonctionne aussi sur un CPU
MODEL_NAME = "runwayml/stable-diffusion-v1-5"

# Paramètres d’inférence
DEVICE = "cpu"  # Afin de forcer l’utilisation du CPU
NUM_INFERENCE_STEPS = 25  
GUIDANCE_SCALE = 7.5  # 7.5 est un bon équilibre entre fidélité au prompt et créativité

# Paramètres de l’image
IMG_HEIGHT = 512 
IMG_WIDTH = 512

# Dossier de sortie pour stocker les images générées
OUTPUT_DIR = "outputs/"
