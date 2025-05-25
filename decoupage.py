import re
import json

def split_by_articles(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    articles = []
    current_part = ""
    current_book = ""
    current_title = ""
    current_chapter = ""
    buffer = ""
    current_article = None

    for line in lines:
        stripped = line.strip()

        if re.match(r"^Partie ", stripped, flags=re.IGNORECASE):
            current_part = stripped
        elif re.match(r"^Livre ", stripped, flags=re.IGNORECASE):
            current_book = stripped
        elif re.match(r"^Titre ", stripped, flags=re.IGNORECASE):
            current_title = stripped
        elif re.match(r"^Chapitre ", stripped, flags=re.IGNORECASE):
            current_chapter = stripped
        elif re.match(r"^Article [A-Z]*L\d{1,6}-\d+\b", stripped):
            # Si on avait un article en cours, on le sauve
            if current_article:
                current_article["texte"] = buffer.strip()
                articles.append(current_article)

            current_article = {
                "partie": current_part,
                "livre": current_book,
                "titre": current_title,
                "chapitre": current_chapter,
                "article_id": stripped.split()[1],
                "texte": ""
            }
            buffer = line  # Commence le nouveau texte
        else:
            buffer += line

    # Ajoute le dernier article
    if current_article:
        current_article["texte"] = buffer.strip()
        articles.append(current_article)

    return articles


if __name__ == "__main__":
    articles = split_by_articles("ingest/code_du_travail_2025.txt")

    print(f"{len(articles)} articles détectés.")
    print("Premier article :\n", articles[0]["texte"][:500])

    # Optionnel : sauvegarde en JSON pour inspection rapide
    with open("ingest/articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)
