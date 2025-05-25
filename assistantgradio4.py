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
        retrieved_docs = vectordb.similarity_search(question, k=3)
        if not retrieved_docs:
            return "Aucune information trouvée."

        context = "\n\n---\n\n".join([doc.page_content for doc in retrieved_docs])

        prompt = f"""
        Tu es un assistant juridique expert du Code du travail 2025.
        Voici des extraits du Code du travail :
        {context}

        Réponds précisément à la question suivante.
        Cite l'article ou la page correspondant à ta réponse.
        Si l'information n'est pas disponible, dis que tu ne sais pas.

        Question : {question}
        """
        response = llm(prompt=prompt, max_tokens=500)
        answer = response['choices'][0]['text'].strip()

        # Liste des sources
        sources = []
        for doc in retrieved_docs:
            meta = doc.metadata
            if 'article' in meta:
                sources.append(meta['article'])
            elif 'page' in meta:
                sources.append(meta['page'])
            elif 'source' in meta:
                sources.append(meta['source'])

        return f"{answer}\n\nSources possibles : {', '.join(sources)}"

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
