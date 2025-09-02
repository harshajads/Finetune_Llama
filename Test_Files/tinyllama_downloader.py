from transformers import AutoModelForCausalLM, AutoTokenizer

# Model repo on Hugging Face
model_name = "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T"

# Download tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("TinyLLaMA downloaded successfully!")
