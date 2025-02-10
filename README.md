### 📄 **`README.md`**
```markdown
# 🎨 Stable Diffusion Image Generator
**Un générateur d'images basé sur Stable Diffusion, utilisant un modèle téléchargé en local.**  
⚡ Fonctionne en CPU ou GPU | 🖼️ Génère des images à partir de texte | 🌍 Interface Gradio interactive  

---

## 📌 Fonctionnalités
✅ Génère des images à partir d'un **prompt textuel**  
✅ **Interface web** avec Gradio  
✅ **Facile à utiliser et à déployer**  

---

## 📂 Structure du Projet
```
IMAGE_GENERATOR_FROM_HUGGING_FACE/
│── env/                  # Environnement virtuel (Crée le vôtre)
│── models/               # Modèles téléchargés (initialement vide)
│── outputs/              # Images générées
│── app.py                # Interface web avec Gradio
│── generate.py           # Génération d'images avec le modèle
│── config.py             # Fichier de configuration (n'hésite pas à le modifier selon vos besoins)
│── requirements.txt      # Dépendances du projet
│── README.md             # Documentation
```

---

## 🚀 Installation et Lancement

### 1️⃣ **Cloner le projet**
```bash
git clone https://github.com/tonpseudo/IMAGE_GENERATOR_FROM_HUGGING_FACE.git
cd IMAGE_GENERATOR_FROM_HUGGING_FACE
```

### 2️⃣ **Créer un environnement virtuel**
```bash
python -m venv env
source env/bin/activate      # Sur macOS/Linux
env\Scripts\activate         # Sur Windows
```

### 3️⃣ **Installer les dépendances**
```bash
pip install -r requirements.txt
```

### **4️⃣ Téléchargement et sauvegarde du modèle**
Exécute `generate.py` une première fois pour télécharger et sauvegarder le modèle :
```bash
python generate.py
```
Cela va :
✅ **Télécharger Stable Diffusion** depuis Hugging Face  
✅ **Générer une première image pour tester**  
✅ **Sauvegarder le modèle localement dans `models/stable-diffusion-cpu`**  

---

### **5️⃣ Modifier `generate.py` pour réutiliser le modèle sauvegardé**
Après la première exécution, modifie `generate.py` et **commente la ligne suivante** :
```python
# pipeline = StableDiffusionPipeline.from_pretrained(MODEL_NAME)
pipeline = StableDiffusionPipeline.from_pretrained("models/stable-diffusion-cpu")
```
Cela **permet de réutiliser le modèle sans le télécharger à chaque fois**.

---

### **6️⃣ Lancer l'application**
Une fois le modèle téléchargé et sauvegardé, lance l'interface Gradio :
```bash
python src/app.py
```
📌 **Accéder à l'interface** : [http://127.0.0.1:7860](http://127.0.0.1:7860)  
---

## 🛠️ Configuration (`config.py`)
```python
MODEL_NAME = "runwayml/stable-diffusion-v1-5"  # Modèle utilisé
DEVICE = "cpu"  # Exécuter en CPU ou GPU
IMG_HEIGHT = 512
IMG_WIDTH = 512
NUM_INFERENCE_STEPS = 25  # Nombre d'itérations pour la génération
OUTPUT_DIR = "outputs/"
```


---

## 🛠️ Dépendances techniques
- [Stable Diffusion (`diffusers`)](https://huggingface.co/docs/diffusers/index)
- [Gradio (interface utilisateur)](https://gradio.app)
- [PyTorch](https://pytorch.org/)

---


## 📜 Licence
Ce projet est sous licence **MIT**. Libre d’utilisation et de modification. 🚀  

```
