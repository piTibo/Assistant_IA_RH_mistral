# Assistant_IA_RH_mistral
Assistant IA RH local — basé sur le Code du travail 2025 🇫🇷

Ce projet est un assistant IA local, conçu pour répondre à des questions liées au Code du travail français, sans dépendance à des services externes (fonctionne entièrement en local).  
Il s'appuie sur un moteur de recherche sémantique avec une base vectorielle Chroma, un modèle LLaMA (Mistral 7B) en .gguf exécuté via llama.cpp, et une interface utilisateur simple grâce à Gradio.

Fonctionnalités principales :
- Indexation automatique du Code du travail 2025 (PDF) en vecteurs.
- Recherche intelligente de passages pertinents à l'aide de langchain et Chroma.
- Génération de réponses en langage naturel via un modèle local Mistral.
- Interface web minimaliste pour poser des questions.

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
