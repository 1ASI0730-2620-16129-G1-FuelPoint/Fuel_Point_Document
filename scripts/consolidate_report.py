#!/usr/bin/env python3
"""
Script de consolidación del Informe Final TB1 para FuelPoint / FullTank.
Concatena README.md y docs/chapter1.md hasta chapter5.md en un único archivo
Markdown listo para exportar a PDF / DOCX con rutas de imágenes y anclas ajustadas.
"""

import os
import re

def consolidate():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(root_dir, "README.md")
    docs_dir = os.path.join(root_dir, "docs")
    output_filename = "upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.md"
    output_path = os.path.join(root_dir, output_filename)

    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    # Reemplazar enlaces internos del TOC: (docs/chapterX.md#ancla) -> (#ancla)
    readme_adjusted = re.sub(r'\(docs/chapter\d+\.md(#.*?)\)', r'(\1)', readme)

    # Separar Front Matter (hasta antes de Conclusiones) y Back Matter (desde Conclusiones)
    conclusiones_marker = "\n## Conclusiones\n"
    if conclusiones_marker in readme_adjusted:
        idx = readme_adjusted.find(conclusiones_marker)
        front_matter = readme_adjusted[:idx].rstrip()
        back_matter = readme_adjusted[idx:].lstrip()
    else:
        front_matter = readme_adjusted
        back_matter = ""

    # Procesar capítulos
    chapters = []
    chapter_files = [f"chapter{i}.md" for i in range(1, 6)]
    for ch_file in chapter_files:
        ch_path = os.path.join(docs_dir, ch_file)
        if not os.path.exists(ch_path):
            print(f"Advertencia: no se encontró {ch_path}")
            continue

        with open(ch_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Ajustar rutas de imágenes relativas para que apunten desde la raíz
        content = content.replace("../assets/", "assets/")
        content = content.replace("../assets-chapter-5/", "assets-chapter-5/")

        # Ajustar enlaces cruzados entre capítulos
        content = re.sub(r'\(docs/chapter\d+\.md(#.*?)\)', r'(\1)', content)
        content = re.sub(r'\(chapter\d+\.md(#.*?)\)', r'(\1)', content)

        chapters.append(content.strip())

    # Consolidar todo el documento
    consolidated_doc = (
        front_matter
        + "\n\n---\n\n"
        + "\n\n---\n\n".join(chapters)
        + "\n\n---\n\n"
        + back_matter
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(consolidated_doc)

    print(f"✅ Informe consolidado generado exitosamente en:\n   {output_path}")
    print(f"📊 Métricas del documento consolidado:")
    print(f"   • Líneas: {len(consolidated_doc.splitlines())}")
    print(f"   • Caracteres: {len(consolidated_doc)}")
    print(f"   • Tamaño: {len(consolidated_doc.encode('utf-8')) / 1024:.1f} KB")

if __name__ == "__main__":
    consolidate()
