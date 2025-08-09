from huggingface_hub import HfApi, login
import os

# Set your Hugging Face token (replace with your actual token or use an environment variable)
HF_TOKEN = os.getenv("HF_TOKEN", "your_hf_token_here")

# Login to Hugging Face
login(token=HF_TOKEN)

api = HfApi()
try:
    api.upload_folder(
        folder_path=".",
        repo_id="samreenss2414/ticket-classifier-model",
        commit_message="Upload ticket classifier model"
    )
    print("Upload successful!")
except Exception as e:
    print(f"Upload failed: {e}")