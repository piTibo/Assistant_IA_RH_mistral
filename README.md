# Assistant_IA_RH_mistral

## 📁 Fichiers volumineux non inclus

Certaines ressources trop volumineuses ne sont **pas versionnées** dans le dépôt. Voici comment les reconstituer :

### 🔹 Base de données Chroma

Le fichier `chroma_code_travail/chroma.sqlite3` est généré automatiquement. Pour le reconstituer, il suffit de lancer :

```bash
python index_articles.py
```
### 🔹 Modèle de langage LLaMA (Mistral)

Le fichier model/mistral-7b-instruct-v0.1.Q4_K_M.gguf peut être téléchargé depuis Hugging Face :

➡️ Téléchargement sur HuggingFace

Modèle recommandé : mistral-7b-instruct-v0.1.Q4_K_M.gguf

Téléchargez-le et placez-le dans le dossier model/.


## Liste des dépendances
```bash
pip install langchain langchain-community langchain-huggingface llama-cpp-python gradio PyMuPDF
```
