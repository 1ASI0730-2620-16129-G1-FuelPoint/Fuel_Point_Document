#!/usr/bin/env python3
"""
Script de consolidación y exportación del Informe Final TB1 para FuelPoint / FullTank.
Genera los archivos directamente en la carpeta 'entregables/':
1. entregables/upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.md
2. entregables/upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.html
3. entregables/upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.pdf (mediante render_pdf.mjs)
"""

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from bs4 import BeautifulSoup

def consolidate():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(root_dir, "README.md")
    docs_dir = os.path.join(root_dir, "docs")
    entregables_dir = os.path.join(root_dir, "entregables")
    os.makedirs(entregables_dir, exist_ok=True)

    md_output = os.path.join(entregables_dir, "upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.md")
    html_output = os.path.join(entregables_dir, "upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.html")
    pdf_output = os.path.join(entregables_dir, "upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.pdf")

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

    print(f"✅ [1/3] Archivo Markdown consolidado generado en entregables:")
    print(f"   Ruta: {md_output}")
    print(f"   Líneas: {len(consolidated_md.splitlines())} | Tamaño: {len(consolidated_md.encode('utf-8')) / 1024:.1f} KB")

    # Compilar a HTML mediante 'marked'
    tmp_html = os.path.join(tempfile.gettempdir(), "marked_report.html")
    try:
        marked_cmd = ["npx.cmd" if os.name == "nt" else "npx", "--yes", "marked", "-i", md_output, "-o", tmp_html]
        subprocess.run(
            marked_cmd,
            shell=True if os.name == "nt" else False,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        with open(tmp_html, "r", encoding="utf-8") as f:
            raw_html_body = f.read()
    except Exception as e:
        print(f"Error compilando con marked: {e}")
        return

    # Post-procesar HTML con BeautifulSoup para garantizar resolución exacta de imágenes y enlaces
    soup = BeautifulSoup(raw_html_body, "html.parser")

    # 1. Normalizar rutas de todas las imágenes a file:/// absolutas
    img_count = 0
    for img in soup.find_all("img"):
        src = img.get("src")
        if not src or src.startswith("http://") or src.startswith("https://") or src.startswith("data:"):
            continue
        clean_src = src.split("#")[0].split("?")[0].strip()
        candidate1 = os.path.normpath(os.path.join(entregables_dir, clean_src))
        candidate2 = os.path.normpath(os.path.join(root_dir, clean_src))
        
        target_path = None
        if os.path.exists(candidate1):
            target_path = candidate1
        elif os.path.exists(candidate2):
            target_path = candidate2
        elif os.path.isabs(clean_src) and os.path.exists(clean_src):
            target_path = clean_src

        if target_path:
            img["src"] = Path(target_path).as_uri()
            img["loading"] = "eager"
            img["decoding"] = "sync"
            img_count += 1
        else:
            print(f"Advertencia: no se encontró archivo para imagen: {src}")

    # 2. Configurar enlaces
    for a in soup.find_all("a"):
        href = a.get("href", "")
        if href.startswith("http://") or href.startswith("https://"):
            a["target"] = "_blank"
            a["rel"] = "noopener noreferrer"

    html_body = str(soup)

    # Plantilla HTML Clásica en Blanco y Negro (con enlaces en azul)
    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FullTank — Informe de Trabajo Parcial (TB1)</title>
  <style>
    @page {{
      size: A4 portrait;
      margin: 20mm 15mm 20mm 15mm;
    }}
    *, *:before, *:after {{
      box-sizing: border-box;
    }}
    body {{
      font-family: Arial, 'Helvetica Neue', Helvetica, 'Liberation Sans', sans-serif;
      font-size: 10.5pt;
      line-height: 1.55;
      color: #000000;
      background-color: #ffffff;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}
    .print-bar {{
      position: sticky;
      top: 0;
      background: #222222;
      color: #ffffff;
      padding: 10px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 1000;
      font-size: 13px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }}
    .print-btn {{
      background: #ffffff;
      color: #000000;
      font-weight: bold;
      border: 1px solid #666666;
      padding: 7px 18px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 13px;
      transition: all 0.2s;
    }}
    .print-btn:hover {{
      background: #e5e5e5;
    }}
    .container {{
      max-width: 900px;
      margin: 20px auto;
      background: #ffffff;
      padding: 40px 60px;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
    }}
    
    /* Encabezados Académicos Clásicos en Blanco y Negro */
    h1, h2, h3, h4, h5, h6 {{
      color: #000000;
      font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
      font-weight: bold;
      page-break-after: avoid;
      break-after: avoid;
    }}
    h1 {{
      font-size: 18pt;
      text-transform: uppercase;
      border-bottom: 2px solid #000000;
      padding-bottom: 6px;
      margin-top: 40px;
      margin-bottom: 18px;
      page-break-before: always;
      break-before: page;
    }}
    h1:first-of-type {{
      page-break-before: avoid;
      break-before: avoid;
      margin-top: 0;
    }}
    h2 {{
      font-size: 14pt;
      border-bottom: 1px solid #000000;
      padding-bottom: 4px;
      margin-top: 28px;
      margin-bottom: 12px;
    }}
    h3 {{
      font-size: 12pt;
      margin-top: 22px;
      margin-bottom: 8px;
    }}
    h4 {{
      font-size: 11pt;
      margin-top: 18px;
      margin-bottom: 6px;
    }}
    h5, h6 {{
      font-size: 10pt;
      margin-top: 14px;
      margin-bottom: 4px;
    }}
    
    p, li {{
      text-align: justify;
      color: #000000;
      margin: 8px 0;
    }}
    ul, ol {{
      padding-left: 24px;
      margin: 8px 0;
    }}
    li {{
      margin-bottom: 4px;
    }}
    
    /* Enlaces: Azules, subrayados y con ajuste de línea para no desbordar */
    a {{
      color: #0056b3;
      text-decoration: underline;
      word-break: break-word;
      overflow-wrap: break-word;
    }}
    a:visited {{
      color: #0056b3;
    }}
    
    /* Tablas: Clásicas en Blanco y Negro alineadas */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 18px 0;
      font-size: 9pt;
      line-height: 1.35;
      page-break-inside: auto;
      table-layout: auto;
    }}
    tr {{
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    th {{
      background-color: #f2f2f2;
      color: #000000;
      font-weight: bold;
      text-align: left;
      padding: 6px 8px;
      border: 1px solid #000000;
      vertical-align: bottom;
    }}
    td {{
      padding: 6px 8px;
      border: 1px solid #000000;
      vertical-align: top;
      color: #000000;
      word-break: break-word;
    }}
    tbody tr:nth-child(even) {{
      background-color: #fafafa;
    }}
    
    /* Imágenes alineadas y escaladas fielmente */
    img {{
      max-width: 100% !important;
      height: auto !important;
      display: block;
      margin: 14px auto;
      page-break-inside: avoid;
      break-inside: avoid;
      image-rendering: -webkit-optimize-contrast;
    }}
    div[align="center"] {{
      text-align: center;
      margin: 14px 0;
    }}
    div[align="center"] img {{
      display: inline-block;
      margin: 0 auto;
    }}
    figure {{
      margin: 14px auto;
      text-align: center;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    figcaption, p > em {{
      color: #222222;
    }}
    
    /* Citas y Bloques de Texto */
    blockquote {{
      border-left: 3px solid #000000;
      margin: 14px 0;
      padding: 8px 14px;
      background: #f8f8f8;
      color: #000000;
      font-style: normal;
    }}
    
    /* Código e Instrucciones */
    code {{
      font-family: Consolas, 'Courier New', Courier, monospace;
      font-size: 8.5pt;
      background: #f2f2f2;
      color: #000000;
      padding: 2px 4px;
      border-radius: 2px;
      border: 1px solid #dcdcdc;
    }}
    pre {{
      background: #f8f8f8;
      color: #000000;
      border: 1px solid #000000;
      padding: 10px 12px;
      border-radius: 4px;
      overflow-x: auto;
      font-size: 8.5pt;
      line-height: 1.4;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    pre code {{
      background: transparent;
      border: none;
      padding: 0;
      color: #000000;
    }}
    
    hr {{
      border: none;
      border-top: 1px solid #000000;
      margin: 28px 0;
    }}
    
    @media print {{
      body {{
        background: #ffffff !important;
        color: #000000 !important;
      }}
      .print-bar {{
        display: none !important;
      }}
      .container {{
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}
      h1 {{
        page-break-before: always;
        break-before: page;
      }}
      h1:first-of-type {{
        page-break-before: avoid;
        break-before: avoid;
      }}
      table, figure, img, pre, blockquote {{
        page-break-inside: avoid;
        break-inside: avoid;
      }}
      a {{
        color: #0056b3 !important;
        text-decoration: underline !important;
      }}
    }}
  </style>
</head>
<body>
  <div class="print-bar">
    <div><strong>FullTank — Informe TB1</strong> (Universidad Peruana de Ciencias Aplicadas · Sección 16129)</div>
    <button class="print-btn" onclick="window.print()">🖨️ Imprimir / Guardar como PDF</button>
  </div>
  <div class="container">
    {html_body}
  </div>
</body>
</html>"""

    with open(html_output, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"✅ [2/3] Archivo HTML clásico generado en entregables ({img_count} imágenes vinculadas):")
    print(f"   Ruta: {html_output}")
    print(f"   Tamaño: {len(html_template.encode('utf-8')) / 1024:.1f} KB")

    # Generar PDF mediante Node.js y puppeteer-core
    render_script = os.path.join(root_dir, "scripts", "render_pdf.mjs")
    fulltank_dir = os.path.join(os.path.dirname(root_dir), "FullTank-trabajo")
    
    print(f"⏳ [3/3] Generando PDF de alta fidelidad con Puppeteer y Edge...")
    try:
        pdf_res = subprocess.run(
            ["node", render_script, html_output, pdf_output],
            cwd=fulltank_dir if os.path.exists(fulltank_dir) else root_dir,
            capture_output=True,
            text=True,
            timeout=240,
            encoding="utf-8"
        )
        print(pdf_res.stdout)
        if pdf_res.returncode != 0:
            print("Error en render_pdf:", pdf_res.stderr)
        
        if os.path.exists(pdf_output) and os.path.getsize(pdf_output) > 0:
            print(f"✅ PDF generado exitosamente en entregables:")
            print(f"   Ruta: {pdf_output}")
            print(f"   Tamaño: {os.path.getsize(pdf_output) / (1024 * 1024):.2f} MB")
            
            # Copiar también al escritorio del usuario para acceso inmediato
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "upc-pre-202620-1asi0730-16129-fuelpoint-report-tb1.pdf")
            shutil.copy2(pdf_output, desktop_path)
            print(f"✅ Copia actualizada en el Escritorio: {desktop_path}")
    except Exception as e:
        print(f"Error generando PDF con Puppeteer: {e}")

if __name__ == "__main__":
    consolidate()
