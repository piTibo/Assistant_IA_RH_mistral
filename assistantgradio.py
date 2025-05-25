from llama_cpp import Llama
import gradio as gr
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Charger le modèle LLaMA
llm = Llama(model_path="model/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=512, n_gpu_layers=20, verbose=False)

# Charger la base vectorielle
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
vectordb = Chroma(persist_directory="chroma_code_travail", embedding_function=embedding_model)


# Fonction principale pour générer une réponse avec citations
def generate_response(question):
    try:
        retrieved_docs = vectordb.similarity_search(question, k=2)

        if not retrieved_docs:
            return "Aucune information trouvée pour répondre à la question."

        # Construire le contexte avec les documents récupérés
        context_parts = []
        source_references = []

        for doc in retrieved_docs:
            context_parts.append(doc.page_content)

            metadata = doc.metadata
            if 'article' in metadata:
                source_references.append(f"article {metadata['article']}")
            elif 'page' in metadata:
                source_references.append(f"page {metadata['page']}")
            elif 'source' in metadata:
                source_references.append(metadata['source'])

        context = "\n\n".join(context_parts)
        sources = ", ".join(set(source_references)) if source_references else "sources inconnues"

        # Prompt avec contexte et demande de citation des sources
        prompt = f"""Voici des extraits issus du Code du travail :

{context}

Réponds à la question suivante de manière précise et concise, en citant les articles ou pages utilisés si possible.

Question : {question}

(Référence(s) utilisée(s) : {sources})
"""

        response = llm(prompt=prompt, max_tokens=500)
        return response['choices'][0]['text'].strip()

    except Exception as e:
        return f"Erreur : {str(e)}"


# Interface Gradio
iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=3, placeholder="Pose ta question..."),
    outputs="text",
    title="Assistant IA RH - Code du travail 2025",
    description="Pose ta question à partir du Code du travail (modèle local, vector DB avec RAG)"
)

if __name__ == "__main__":
    iface.launch()
