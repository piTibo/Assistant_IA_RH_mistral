# Assistant_IA_RH_mistral

## 📁 Fichiers volumineux non inclus

Certaines ressources trop volumineuses ne sont **pas versionnées** dans le dépôt. Voici comment les reconstituer :

### 🔹 Base de données Chroma

Le fichier `chroma_code_travail/chroma.sqlite3` est généré automatiquement. Pour le reconstituer, il suffit de lancer :

```bash
python index_articles.py

## Liste des dépendances
pip install langchain langchain-community langchain-huggingface llama-cpp-python gradio PyMuPDF
