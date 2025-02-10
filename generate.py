import torch
from diffusers import StableDiffusionPipeline
import os
from config import MODEL_NAME, DEVICE, NUM_INFERENCE_STEPS, GUIDANCE_SCALE, IMG_HEIGHT, IMG_WIDTH, OUTPUT_DIR
from datetime import datetime

print(f" Using device: {DEVICE}")

#  Charger le modèle Stable Diffusion
print(" Loading Stable Diffusion model...")
#pipeline = StableDiffusionPipeline.from_pretrained(MODEL_NAME)
pipeline = StableDiffusionPipeline.from_pretrained("models/stable-diffusion-cpu")
pipeline.to(DEVICE)  

# Fonction pour générer une image
def generate_image(prompt):
  
    print(f" Generating image for prompt: {prompt}")
    image = pipeline(
        prompt,
        num_inference_steps=NUM_INFERENCE_STEPS,
        guidance_scale=GUIDANCE_SCALE,
        height=IMG_HEIGHT,
        width=IMG_WIDTH
    ).images[0]

    #  Sauvegarde de l'image
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(OUTPUT_DIR, f"generated_{timestamp}.png")
    image.save(file_path)
    
    print(f"Image saved at: {file_path}")
    return file_path

# Tester la génération avec un exemple
if __name__ == "__main__":
    test_prompt = "A futuristic city at sunset with flying cars"
    generate_image(test_prompt)
