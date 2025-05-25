from llama_cpp import Llama

MODEL_PATH = "model/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_gpu_layers=20,  # Nombre de couches sur GPU (ajuste si besoin)
    n_ctx=2048,
    verbose=True
)

prompt = "Quelle est la capitale de la France ?"

response = llm(prompt=prompt, max_tokens=50)
print(response['choices'][0]['text'])