#!/usr/bin/env python3
"""
Script de consolidación y exportación del Informe Final TB1 para FuelPoint / FullTank.
Genera los archivos directamente en la carpeta 'entregables/':
1. entregables/upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.md
2. entregables/upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.html
"""

import os
import re
import shutil
import subprocess

def consolidate():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(root_dir, "README.md")
    docs_dir = os.path.join(root_dir, "docs")
    entregables_dir = os.path.join(root_dir, "entregables")
    os.makedirs(entregables_dir, exist_ok=True)

    md_output = os.path.join(entregables_dir, "upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.md")
    html_output = os.path.join(entregables_dir, "upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.html")

    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    # Ajustar rutas de imagen de la carátula y assets para entregables/
    readme_adjusted = readme.replace('src="logo_upc.PNG"', 'src="../logo_upc.PNG"')
    readme_adjusted = readme_adjusted.replace('(assets/', '(../assets/')

    # Reemplazar enlaces internos del TOC: (docs/chapterX.md#ancla) -> (#ancla)
    readme_adjusted = re.sub(r'\(docs/chapter\d+\.md(#.*?)\)', r'(\1)', readme_adjusted)

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

        # Las imágenes en docs/chapter*.md ya apuntan a ../assets/ y ../assets-chapter-5/
        # lo cual es exactamente la ruta correcta desde entregables/

        # Ajustar enlaces cruzados entre capítulos
        content = re.sub(r'\(docs/chapter\d+\.md(#.*?)\)', r'(\1)', content)
        content = re.sub(r'\(chapter\d+\.md(#.*?)\)', r'(\1)', content)

        chapters.append(content.strip())

    # Consolidar todo el documento Markdown
    consolidated_md = (
        front_matter
        + "\n\n---\n\n"
        + "\n\n---\n\n".join(chapters)
        + "\n\n---\n\n"
        + back_matter
    )

    with open(md_output, "w", encoding="utf-8") as f:
        f.write(consolidated_md)

    print(f"✅ [1/2] Archivo Markdown consolidado generado en entregables:")
    print(f"   Ruta: {md_output}")
    print(f"   Líneas: {len(consolidated_md.splitlines())} | Tamaño: {len(consolidated_md.encode('utf-8')) / 1024:.1f} KB")

    # Compilar a HTML mediante 'marked'
    tmp_html = "/tmp/marked_report.html"
    try:
        subprocess.run(
            ["npx", "--yes", "marked", "-i", md_output, "-o", tmp_html],
            check=True,
            capture_output=True,
            text=True
        )
        with open(tmp_html, "r", encoding="utf-8") as f:
            html_body = f.read()
    except Exception as e:
        print(f"Error compilando con marked: {e}")
        return

    # Plantilla HTML con estilo académico formal y soporte de impresión PDF
    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FullTank — Informe de Trabajo Parcial (TB1)</title>
  <style>
    @page {{
      size: A4;
      margin: 20mm 15mm 20mm 15mm;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-size: 11pt;
      line-height: 1.6;
      color: #1f2937;
      background-color: #f3f4f6;
      margin: 0;
      padding: 0;
    }}
    .print-bar {{
      position: sticky;
      top: 0;
      background: #1e3a8a;
      color: white;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 1000;
      box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }}
    .print-btn {{
      background: #fbbf24;
      color: #1e3a8a;
      font-weight: bold;
      border: none;
      padding: 10px 22px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 14px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.2);
      transition: all 0.2s;
    }}
    .print-btn:hover {{
      background: #f59e0b;
      transform: translateY(-1px);
    }}
    .container {{
      max-width: 960px;
      margin: 24px auto;
      background: #ffffff;
      padding: 50px 70px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
    }}
    h1 {{
      font-size: 22pt;
      color: #1e3a8a;
      border-bottom: 2px solid #1e3a8a;
      padding-bottom: 8px;
      margin-top: 48px;
      page-break-before: always;
    }}
    h1:first-of-type {{
      page-break-before: avoid;
    }}
    h2 {{
      font-size: 16pt;
      color: #1e40af;
      border-bottom: 1px solid #e5e7eb;
      padding-bottom: 4px;
      margin-top: 36px;
    }}
    h3 {{
      font-size: 13pt;
      color: #1f2937;
      margin-top: 24px;
    }}
    h4 {{
      font-size: 11.5pt;
      color: #374151;
      margin-top: 18px;
    }}
    p, li {{
      text-align: justify;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      font-size: 9.5pt;
      page-break-inside: auto;
    }}
    tr {{
      page-break-inside: avoid;
      page-break-after: auto;
    }}
    th {{
      background-color: #1e3a8a;
      color: #ffffff;
      font-weight: 600;
      text-align: left;
      padding: 8px 10px;
      border: 1px solid #1e3a8a;
    }}
    td {{
      padding: 6px 10px;
      border: 1px solid #d1d5db;
      vertical-align: top;
    }}
    tbody tr:nth-child(even) {{
      background-color: #f9fafb;
    }}
    img {{
      max-width: 100%;
      height: auto;
      display: block;
      margin: 16px auto;
      border-radius: 4px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    }}
    code {{
      font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
      font-size: 9pt;
      background: #f3f4f6;
      padding: 2px 5px;
      border-radius: 4px;
      color: #b91c1c;
    }}
    pre {{
      background: #1f2937;
      color: #f9fafb;
      padding: 14px;
      border-radius: 6px;
      overflow-x: auto;
      font-size: 9pt;
      line-height: 1.45;
    }}
    pre code {{
      background: transparent;
      color: inherit;
      padding: 0;
    }}
    blockquote {{
      border-left: 4px solid #1e3a8a;
      margin: 16px 0;
      padding: 8px 16px;
      background: #eff6ff;
      color: #1e3a8a;
    }}
    hr {{
      border: none;
      border-top: 1px solid #e5e7eb;
      margin: 36px 0;
    }}
    a {{
      color: #2563eb;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    @media print {{
      body {{
        background: white;
      }}
      .print-bar {{
        display: none !important;
      }}
      .container {{
        box-shadow: none;
        padding: 0;
        margin: 0;
        max-width: 100%;
        border-radius: 0;
      }}
      h1 {{
        page-break-before: always;
      }}
      table, figure, img {{
        page-break-inside: avoid;
      }}
    }}
  </style>
</head>
<body>
  <div class="print-bar">
    <div><strong>FullTank — Informe TB1</strong> (Universidad Peruana de Ciencias Aplicadas · Sección 16129)</div>
    <button class="print-btn" onclick="window.print()">🖨️ Imprimir / Guardar como PDF (Ctrl + P)</button>
  </div>
  <div class="container">
    {html_body}
  </div>
</body>
</html>"""

    with open(html_output, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"✅ [2/2] Archivo HTML listo para exportar generado en entregables:")
    print(f"   Ruta: {html_output}")
    print(f"   Tamaño: {len(html_template.encode('utf-8')) / 1024:.1f} KB")

    # Copiar también a /home/bryan/code/Proyectos/FullTank/entregables/
    parent_entregables = "/home/bryan/code/Proyectos/FullTank/entregables"
    if os.path.exists(parent_entregables):
        shutil.copy2(md_output, parent_entregables)
        shutil.copy2(html_output, parent_entregables)
        print(f"✅ Copia sincronizada en carpeta general de entregables:")
        print(f"   Ruta: {parent_entregables}/")

if __name__ == "__main__":
    consolidate()
