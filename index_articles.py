from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Chargement et découpage des documents
loader = TextLoader("ingest/code_du_travail_2025.txt", encoding="utf-8")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# Création du modèle d'embeddings avec la nouvelle classe
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# Création de la base vectorielle
vectordb = Chroma.from_documents(
    documents=texts,
    embedding=embedding_model,
    persist_directory="chroma_code_travail"
)

# Pas besoin d'appeler vectordb.persist() maintenant, c'est automatique

print("✅ Base vectorielle créée et persistée dans chroma_code_travail")