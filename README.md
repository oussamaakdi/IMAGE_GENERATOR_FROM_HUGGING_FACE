### 📄 **README.md**
```markdown
# 🎨 Stable Diffusion Image Generator
Générateur d'images basé sur **Stable Diffusion**, utilisant un modèle local.  
🚀 Fonctionne en CPU ou GPU | 🖼️ Interface Gradio  

---

## 📌 Fonctionnalités
- 📝 Génère des images à partir d'un **prompt**  
- 🌍 Interface web **Gradio**  
- ⚡ Facile à installer et utiliser  

---

## 📂 Structure du Projet
```
IMAGE_GENERATOR_FROM_HUGGING_FACE/
│── env/                  # Environnement virtuel (à créer)
│── models/               # Modèle téléchargé (sauvegardé ici)
│── outputs/              # Images générées
│── app.py                # Interface web
│── generate.py           # Génération d'images
│── config.py             # Configuration
│── requirements.txt      # Dépendances
│── README.md             # Documentation
```

---

## 🚀 Installation et Utilisation

### **1️⃣ Cloner le projet**
```bash
git clone https://github.com/tonpseudo/IMAGE_GENERATOR_FROM_HUGGING_FACE.git
cd IMAGE_GENERATOR_FROM_HUGGING_FACE
```

### **2️⃣ Créer un environnement virtuel**
```bash
python -m venv env
source env/bin/activate      # macOS/Linux
env\Scripts\activate         # Windows
```

### **3️⃣ Installer les dépendances**
```bash
pip install -r requirements.txt
```

### **4️⃣ Télécharger et sauvegarder le modèle**
Exécute `generate.py` pour télécharger le modèle :
```bash
python generate.py
```
✅ **Télécharge le modèle**  
✅ **Génère une image test**  
✅ **Sauvegarde dans `models/stable-diffusion-cpu`**  

---

### **5️⃣ Modifier `generate.py` pour éviter le téléchargement à chaque fois**
Après la première exécution, modifie `generate.py` et **commente la ligne suivante** :
```python
# pipeline = StableDiffusionPipeline.from_pretrained(MODEL_NAME)
pipeline = StableDiffusionPipeline.from_pretrained("models/stable-diffusion-cpu")
```

---

### **6️⃣ Lancer l'application**
```bash
python app.py
```
📌 **Accéder à l'interface** : [http://127.0.0.1:7860](http://127.0.0.1:7860)  

---

## ⚙️ Configuration (`config.py`)
```python
MODEL_NAME = "runwayml/stable-diffusion-v1-5"
DEVICE = "cpu"
IMG_HEIGHT = 512
IMG_WIDTH = 512
NUM_INFERENCE_STEPS = 25
OUTPUT_DIR = "outputs/"
```

---

## 🛠️ Dépendances
- **[`diffusers`](https://huggingface.co/docs/diffusers/index)**
- **[`Gradio`](https://gradio.app)**
- **[`PyTorch`](https://pytorch.org/)**

---

## 📜 Licence
Projet sous licence **MIT**. Libre d’utilisation et modification. 🚀  
```

---

### **🎯 Changements par rapport à la version précédente**
✅ Markdown **plus simple et épuré**  
✅ Moins de **gras et emojis**, juste ce qu'il faut  
✅ **Instructions claires et concises**  

**📌 Dis-moi si c'est bon ou si tu veux encore plus simple !** 🚀
