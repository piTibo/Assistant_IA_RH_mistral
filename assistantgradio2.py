from llama_cpp import Llama
import gradio as gr
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Paramètres
MODEL_PATH = "model/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
N_CTX = 2048  # Augmentation du contexte (à ajuster selon GPU)

# Charger le modèle LLaMA
llm = Llama(model_path=MODEL_PATH, n_ctx=N_CTX, n_gpu_layers=20, verbose=False)

# Charger la base vectorielle
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
vectordb = Chroma(persist_directory="chroma_code_travail", embedding_function=embedding_model)

def generate_response(question):
    try:
        # Récupérer au max 1 ou 2 documents pour limiter la taille
        retrieved_docs = vectordb.similarity_search(question, k=1)

        if not retrieved_docs:
            return "Aucune information trouvée pour répondre à la question."

        # Concaténer les textes tout en limitant la taille à N_CTX - tokens_question - marge
        # Simple approche : ne prendre qu'un seul doc (k=1 ci-dessus) pour éviter le dépassement

        context = retrieved_docs[0].page_content

        metadata = retrieved_docs[0].metadata
        source = "source inconnue"
        if 'article' in metadata:
            source = f"article {metadata['article']}"
        elif 'page' in metadata:
            source = f"page {metadata['page']}"
        elif 'source' in metadata:
            source = metadata['source']

        prompt = f"""Voici un extrait du Code du travail :

{context}

Réponds à la question suivante de manière précise et concise, en citant l'article ou la page utilisée si possible.

Question : {question}

(Référence utilisée : {source})
"""

        response = llm(prompt=prompt, max_tokens=500)
        return response['choices'][0]['text'].strip()

    except Exception as e:
        return f"Erreur : {str(e)}"

iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=3, placeholder="Pose ta question..."),
    outputs="text",
    title="Assistant IA RH - Code du travail 2025",
    description="Pose ta question à partir du Code du travail (modèle local, vector DB avec RAG)"
)

if __name__ == "__main__":
    iface.launch()
