# Assistant_IA_RH_mistral
Assistant IA RH local — basé sur le Code du travail 2025 🇫🇷

Ce projet est un assistant IA local, conçu pour répondre à des questions liées au Code du travail français, sans dépendance à des services externes (fonctionne entièrement en local).  
Il s'appuie sur un moteur de recherche sémantique avec une base vectorielle Chroma, un modèle LLaMA (Mistral 7B) en .gguf exécuté via llama.cpp, et une interface utilisateur simple grâce à Gradio.

Fonctionnalités principales :
- Indexation automatique du Code du travail 2025 (PDF) en vecteurs.
- Recherche intelligente de passages pertinents à l'aide de langchain et Chroma.
- Génération de réponses en langage naturel via un modèle local Mistral.
- Interface web minimaliste pour poser des questions.

Fiche Projet — Assistant IA Juridique Local (Code du travail 2025)
Objectif

Développer un assistant intelligent capable de répondre à des questions juridiques précises basées sur le Code du travail 2025, en s’appuyant sur une approche Retrieval-Augmented Generation (RAG) pour citer précisément les articles concernés.
Fonctionnalités principales

    Recherche documentaire via une base vectorielle construite à partir du texte du Code du travail.

    Génération de réponses contextualisées à partir d’un modèle de langage local (Mistral 7B instruct quantifié).

    Citation des articles précis utilisés pour appuyer les réponses.

    Interface utilisateur simple via Gradio pour poser les questions en langage naturel.

Technologies utilisées

    Modèle de langage : Mistral 7B instruct quantifié (mistral-7b-instruct-v0.1.Q4_K_M.gguf) chargé via la bibliothèque llama_cpp.

    Indexation et recherche :

        Embeddings générés avec sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 via langchain_huggingface.

        Vector store basé sur Chroma pour stocker et rechercher les passages pertinents.

    Chaîne RAG construite avec langchain RetrievalQA combinant le retriever Chroma et le modèle local.

    Interface Web : développée avec Gradio pour une interaction facile en local.

Points techniques et défis

    Gestion du contexte et limite de tokens (n_ctx=512 avec le modèle local).

    Mise en place d’une récupération efficace des documents pertinents (max 2 documents pour éviter overflow).

    Amélioration de la génération pour éviter les hallucinations et réponses hors sujet (ex. générer plusieurs Q/R non demandées).

    Citation automatique des sources (articles du Code du travail) dans la réponse.

    Intégration et quantification du modèle local pour performance GPU (RTX 3060 Ti).

Enjeux métiers

    Fournir un assistant fiable et précis pour les questions juridiques, utile aux RH, juristes, et collaborateurs.

    Automatiser l’accès aux textes complexes et volumineux (Code du travail).

    Améliorer l’expérience utilisateur avec des réponses argumentées et sourcées.

Perspectives d’évolution

    Optimiser le prompt et la génération pour des réponses plus ciblées.

    Intégrer la gestion des versions et mises à jour du Code du travail.

    Ajouter des fonctionnalités de synthèse ou de comparaison entre articles.

    Déploiement possible sur serveur local sécurisé ou intranet d’entreprise.

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
