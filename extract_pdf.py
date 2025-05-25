import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path, output_txt_path=None):
    doc = fitz.open(pdf_path)
    all_text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        all_text += f"\n\n--- Page {page_num + 1} ---\n{text}"

    if output_txt_path:
        with open(output_txt_path, "w", encoding="utf-8") as f:
            f.write(all_text)
        print(f"Texte extrait sauvegardé dans : {output_txt_path}")

    return all_text

# Exemple d'utilisation
pdf_path = "data/code_du_travail_2025.pdf"  # à adapter à ton chemin réel
output_path = "ingest/code_du_travail_2025.txt"

full_text = extract_text_from_pdf(pdf_path, output_path)