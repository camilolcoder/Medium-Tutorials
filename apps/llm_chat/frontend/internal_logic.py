from gradio_client import Client
import shutil
import os
import time

def generate_image_from_text(prompt:str):
    client = Client("black-forest-labs/FLUX.1-dev")
    result = client.predict(
            prompt=prompt,
            seed=0,
            randomize_seed=True,
            width=512,#1024,
            height=512,#1024,
            guidance_scale=3.5,
            num_inference_steps=28,
            api_name="/infer"
    )
    print(result)

    # Extract the image path from the result
    image_path = result[0]  # First element of the tuple is the image file path

    # Get the current working directory
    destination_folder = os.getcwd()  # This gets the folder where the script is running

    # Define the new file path
    new_image_path = os.path.join(destination_folder, os.path.basename(image_path))

    # Move the image to the new location
    shutil.move(image_path, new_image_path)

    # Ensure the image is fully moved before returning
    time.sleep(1)  # Small delay to avoid file handling issues

    print(f"Image saved to: {new_image_path}")

    return new_image_path

# from huggingface_hub import login
# login()