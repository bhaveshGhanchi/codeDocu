from huggingface_hub import HfApi
import os
api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="gpt2-docstring-model",
    repo_id="ghanchi/gpt2-docstring-generator",
    repo_type="model",
)
