import gradio as gr
from generate import generate_image

def generate_and_display(prompt):
    image_path = generate_image(prompt)  
    return image_path  

with gr.Blocks() as demo:
    gr.Markdown("Stable Diffusion - Image Generator")
    gr.Markdown("Entrez une description et obtenez une image générée par IA !")

    with gr.Row():
        prompt_input = gr.Textbox(label="Entrez votre prompt ici :", placeholder="Un chaton dans l'espace...")
        generate_button = gr.Button("Générer l'image")

    image_output = gr.Image(label="Image Générée")

    generate_button.click(fn=generate_and_display, inputs=prompt_input, outputs=image_output)

if __name__ == "__main__":
    demo.launch()
