from fastapi import FastAPI
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoTokenizer, AutoModelForCausalLM
import torch
import uvicorn

app = FastAPI()

# Load GPT-2 model and tokenizer
MODEL_PATH = "./gpt2-docstring-model"  # Replace with your checkpoint path
model_id = 'ghanchi/gpt2-docstring-generator'
# Load the fine-tuned model and tokenizer
# model = GPT2LMHeadModel.from_pretrained("./gpt2-docstring-model")
# tokenizer = GPT2Tokenizer.from_pretrained("./gpt2-docstring-model")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

class CodeRequest(BaseModel):
    code: str

@app.post("/generate-docstring")
def generate_docstring(request: CodeRequest):
    
    prompt = f"<s> {request.code} </s> <sep>"
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    input_len = input_ids.shape[1]
    outputs = model.generate(
        input_ids,
        max_length=input_len + 50,  # buffer for generation
        num_beams=9,
        no_repeat_ngram_size=4,
        early_stopping=True,
        pad_token_id=tokenizer.eos_token_id
    )
    generated_ids = outputs[0][input_len:]  # exclude prompt
    result = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
    return {"docstring": result}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)